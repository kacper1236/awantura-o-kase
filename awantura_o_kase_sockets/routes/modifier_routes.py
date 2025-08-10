from flask_socketio import emit
from database.Entity.competitor import *
from database.Entity.round import *
from extentions import db

def register_modifier_socketio_handlers(socketio):
    @socketio.on('punish_competitor')
    def handle_punish_competitor(data):
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
        try:
            with db.session.begin_nested():
                reset_temp_money(db, team)
                subtrack(db, team, money)
            db.session.commit()
            emit('competitor_punished', {'message': 'Competitor punished successfully', 'team': team, 'money': money}, broadcast=True)
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
            with db.session.begin_nested():
                subtrack(db, team, money)
                add_hint_to_competitor(db, team)
            db.session.commit()
            emit('hint_bought', {'message': 'Hint bought successfully', 'team': team}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('buy_pack_lost_player')
    def handle_buy_pack_lost_player(data):
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
        if not is_competitors_bidding(db):
            emit('error', {'error': 'Round is not bidding. Competitors cannot buy pack lost player.'})
            return
        if not is_lost_player(db, team):
            emit('error', {'error': f'Team {team} is not lost player'})
            return
        try:
            with db.session.begin_nested():
                subtrack(db, team, money)
                change_lost_player(db, team)
            db.session.commit()
            emit('pack_lost_player_bought', {'message': 'Pack lost player bought successfully', 'team': team}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('buy_blackbox')
    def handle_buy_blackbox(data):
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
            with db.session.begin_nested():
                subtrack(db, team, money)
                add_blackbox_to_competitor(db, team)
            db.session.commit()
            emit('blackbox_bought', {'message': 'Blackbox bought successfully', 'team': team}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('one_vs_one_step_1')
    def handle_one_vs_one_step_1(data):
        team1 = data.get('team1')
        team2 = data.get('team2')

        if not team1 or not team2:
            emit('error', {'error': 'Team names cannot be empty'})
            return
        if team1 == team2:
            emit('error', {'error': 'Teams cannot be the same'})
            return
        if not is_playing(db, team1) or not is_playing(db, team2):
            emit('error', {'error': 'One or both teams are not playing'})
            return
        try:
            with db.session.begin_nested():
                subtrack(db, team1, 500)
                subtrack(db, team2, 500)
                change_onevsone(db, [team1, team2])
            db.session.commit()
            emit('one_vs_one_started', {'message': 'One vs One challenge initiated successfully', 'teams': [team1, team2]}, broadcast=True)
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

    @socketio.on('one_vs_one_step_2')
    def handle_one_vs_one_step_2(data):
        team1 = data.get('team1')
        team2 = data.get('team2')

        if not team1 or not team2:
            emit('error', {'error': 'Team names cannot be empty'})
            return
        if team1 == team2:
            emit('error', {'error': 'Teams cannot be the same'})
            return
        if not is_playing(db, team1) or not is_playing(db, team2):
            emit('error', {'error': 'One or both teams are not playing'})
            return

    @socketio.on('one_vs_one_step_3')
    def handle_one_vs_one_step_3(data):
        team1 = data.get('team1')
        team2 = data.get('team2')
        winner = data.get('winner')

        if not winner:
            emit('error', {'error': 'Winner cannot be empty'})
            return
        if winner not in [team1, team2]:
            emit('error', {'error': 'Winner must be one of the teams'})
            return
        if not team1 or not team2:
            emit('error', {'error': 'Team names cannot be empty'})
            return
        if team1 == team2:
            emit('error', {'error': 'Teams cannot be the same'})
            return
        if not is_playing(db, team1) or not is_playing(db, team2):
            emit('error', {'error': 'One or both teams are not playing'})
            return
        try:
            with db.session.begin_nested():
                reset_temp_money(db, team1)
                reset_temp_money(db, team2)
                change_onevsone(db, [team1, team2])
                if winner == team1:
                    add_money(db, team1)
                else:
                    add_money(db, team2)
            db.session.commit()
            emit('one_vs_one_completed', {'message': 'One vs One challenge completed successfully', 'teams': [team1, team2]}, broadcast=True)   
        except Exception as e:
            db.session.rollback()
            emit('error', {'error': str(e)})

