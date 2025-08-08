from flask_socketio import emit
from database.Entity.round import *
from database.Entity.pool import *
from database.Entity.competitor import *
from extentions import db

def register_round_socketio_handlers(socketio):
    @socketio.on('reset_round')
    def handle_reset_round():
        try:
            reset_round(db)
            emit('round_reset', {'message': 'Round reset successfully'}, broadcast=True)
        except Exception as e:
            emit('error', {'error': str(e)})

    @socketio.on('next_round')
    def handle_next_round():
        try:
            with db.session.begin_nested():
                next_round(db)
                take_money_to_next_round(db)
                assign_pool_for_new_round(db)
                open_round(db)
            db.session.commit()
            emit('next_round_started', {'message': 'Next round started successfully'}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('get_round')
    def handle_get_round():
        try:
            round_info = get_round(db)
            if round_info:
                emit('round_data', round_info)
            else:
                emit('error', {'error': 'No round data found'})
        except Exception as e:
            emit('error', {'error': str(e)})

    @socketio.on('close_round')
    def handle_close_round():
        try:
            reset_temp_money_all(db)
            with db.session.begin_nested():
                close_round(db)
            db.session.commit()
            emit('round_closed', {'message': 'Round closed successfully'}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('buy_hint')
    def handle_buy_hint(data):
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
        if not is_bidded(db, team):
            emit('error', {'error': f'Team {team} has not bidded'})
            return
        try:
            if get_hint_for_competitor(db, team) > 0:
                with db.session.begin_nested():
                    substract_hint_from_competitor(db, team)
                db.session.commit()
                emit('hint_used', {'message': 'Hint used successfully', 'team': team}, broadcast=True)
            else:
                with db.session.begin_nested():
                    subtrack(db, team, money)
                    add_hint_to_competitor(db, team)
                db.session.commit()
                emit('hint_bought', {'message': 'Hint bought successfully', 'team': team}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})
