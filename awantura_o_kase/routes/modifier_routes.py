from flask import Blueprint
from database.Entity.competitor import *
from database.Entity.round import *
from extentions import db

modifier_bp = Blueprint('modifier', __name__)

@modifier_bp.route('/punish-competitor/<team>/<int:money>', methods=['POST'])
def punish_competitor_route(team, money):
    if not isinstance(money, int):
        return {'error': 'Money must be an integer'}, 400
    if money <= 0:
        return {'error': 'Money cannot be negative'}, 400
    if not team:
        return {'error': 'Team name cannot be empty'}, 400
    if not is_playing(db, team):
        return {'error': f'Team {team} is not playing'}, 400
    try:
        with db.session.begin_nested():
            reset_temp_money(db, team)
            subtrack(db, team, money)
        db.session.commit()
        return {'message': 'Competitor punished successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
    
@modifier_bp.route('/buy-hint/<team>/<int:money>', methods=['POST'])
def buy_hint_route(team, money): #użycie tylko po wybraniu z koła pola podpowiedź
    if not isinstance(money, int):
        return {'error': 'Money must be an integer'}, 400
    if money <= 0:
        return {'error': 'Money cannot be negative'}, 400
    if not team:
        return {'error': 'Team name cannot be empty'}, 400
    if not is_playing(db, team):
        return {'error': f'Team {team} is not playing'}, 400
    if not is_bidded(db, team):
        return {'error': f'Team {team} has not bidded'}, 400
    try:
        with db.session.begin_nested():
            subtrack(db, team, money)
            add_hint_to_competitor(db, team)
        db.session.commit()
        return {'message': 'Hint bought successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

@modifier_bp.route('/buypack-lost-player/<team>/<int:money>', methods=['POST'])
def buypack_lost_player_route(team, money):
    if not isinstance(money, int):
        return {'error': 'Money must be an integer'}, 400
    if money <= 0:
        return {'error': 'Money cannot be negative'}, 400
    if not team:
        return {'error': 'Team name cannot be empty'}, 400
    if not is_playing(db, team):
        return {'error': f'Team {team} is not playing'}, 400
    if not is_bidded(db, team):
        return {'error': f'Team {team} has not bidded'}, 400
    if not is_competitors_bidding(db):
        return {'error': 'Round is not bidding. Competitors cannot buy pack lost player.'}, 400
    if not is_lost_player(db, team):
        return {'error': f'Team {team} is not lost player'}, 400
    try:
        with db.session.begin_nested():
            subtrack(db, team, money)
            change_lost_player(db, team)
        db.session.commit()
        return {'message': 'Pack lost player bought successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

@modifier_bp.route('/buy-blackbox/<team>/<int:money>', methods=['POST'])
def buy_blackbox_route(team, money):
    if not isinstance(money, int):
        return {'error': 'Money must be an integer'}, 400
    if money <= 0:
        return {'error': 'Money cannot be negative'}, 400
    if not team:
        return {'error': 'Team name cannot be empty'}, 400
    if not is_playing(db, team):
        return {'error': f'Team {team} is not playing'}, 400
    if not is_bidded(db, team):
        return {'error': f'Team {team} has not bidded'}, 400
    try:
        with db.session.begin_nested():
            subtrack(db, team, money)
            add_blackbox_to_competitor(db, team)
        db.session.commit()
        return {'message': 'Blackbox bought successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

@modifier_bp.route('/onevsone_step_1/<team1>/<team2>', methods=['POST'])
def one_vs_one_step_1_route(team1, team2):
    if not team1 or not team2:
        return {'error': 'Team names cannot be empty'}, 400
    if not is_playing(db, team1) or not is_playing(db, team2):
        return {'error': f'One or both teams are not playing'}, 400
    if team1 == team2:
        return {'error': 'Teams cannot be the same'}, 400
    try:
        with db.session.begin_nested():
            subtrack(db, team1, 500)
            subtrack(db, team2, 500)
            change_onevsone(db, [team1, team2])
        db.session.commit()
        return {'message': 'One vs One challenge initiated successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

@modifier_bp.route('/onevsone_step_2/<team1>/<team2>', methods=['POST'])
def one_vs_one_step_2_route(team1, team2):
    if not team1 or not team2:
        return {'error': 'Team names cannot be empty'}, 400
    if not is_playing(db, team1) or not is_playing(db, team2):
        return {'error': f'One or both teams are not playing'}, 400
    if team1 == team2:
        return {'error': 'Teams cannot be the same'}, 400
    #dopisać wybór ostatniej kategorii :v 

#dopisać etap 3 na 1 na 1 oraz resetowanie flaci 1 na 1
