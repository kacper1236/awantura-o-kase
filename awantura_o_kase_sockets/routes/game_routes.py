from flask_socketio import emit
from database.Entity.round import *
from database.Entity.pool import *
from database.Entity.competitor import *
from extentions import db

def register_game_socketio_handlers(socketio):
    @socketio.on('reset_game')
    def handle_reset_game():
        try:
            global_reset_round(db)
            reset_pool(db)
            reset_competitors(db)
            emit('game_reset_success', {'message': 'Game reset successfully'}, broadcast=True)
        except Exception as e:
            emit('error', {'error': str(e)})

    @socketio.on('add_to_pool')
    def handle_add_to_pool(data):
        team = data.get('team')
        money = data.get('money')

        if not isinstance(money, int):
            emit('error', {'error': 'Money must be an integer'})
            return
        if money <= 0:
            emit('error', {'error': 'Money cannot be negative'})
            return
        if not team:
            emit('error', {'error': 'Team name cannot be empty'})
            return
        if not is_playing(db, team):
            emit('error', {'error': f'Team {team} is not playing'})
            return
        if is_bidded(db, team):
            emit('error', {'error': f'Team {team} has already bidded'})
            return
        if not is_competitors_bidding(db):
            emit('error', {'error': 'Round is not bidding. Competitors cannot add to pool.'})
            return

        try:
            with db.session.begin_nested():
                add_pool(db, team, money)
                subtrack(db, team, money)
                add_temp_money(db, team, money)
                maximize_bet(db, team, money)
                change_bidded(db, team)
            db.session.commit()
            emit('pool_update', {'message': f'Added {money} to {team} pool', 'team': team, 'money': money}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('reset_temp_money')
    def handle_reset_temp_money():
        try:
            reset_temp_money(db)
            emit('temp_money_reset', {'message': 'Reset temporary money'}, broadcast=True)
        except Exception as e:
            emit('error', {'error': str(e)})
