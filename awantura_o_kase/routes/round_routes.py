from flask import Blueprint
from database.Entity.round import *
from database.Entity.pool import *
from database.Entity.competitor import *
from extentions import db

round_bp = Blueprint('round', __name__)

@round_bp.route('/reset-round', methods=['POST'])
def reset_round_route():
    try:
        reset_round(db)
        return {'message': 'Round reset successfully'}, 200
    except Exception as e:
        return {'error': str(e)}, 400
    
@round_bp.route('/next-round', methods=['POST'])
def next_round_route():
    try:
        with db.session.begin_nested():
            next_round(db)
            take_money_to_next_round(db)
            assign_pool_for_new_round(db)
            open_round(db)
        db.session.commit()
        return {'message': 'Next round started successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
    
@round_bp.route('/get-round', methods=['GET'])
def get_round_route():
    try:
        round_info = get_round(db)
        if round_info:
            return round_info, 200
        return {'error': 'No round data found'}, 404
    except Exception as e:
        return {'error': str(e)}, 400
    
@round_bp.route('/close-round', methods=['POST'])
def close_round_route(): #zamknięcie licytacji
    try:
        reset_temp_money_all(db)
        with db.session.begin_nested():
            close_round(db)
        db.session.commit()
        return {'message': 'Round closed successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
    
@round_bp.route('/buy-hint/<team>/<int:money>', methods=['POST'])
def buy_hint_route(team, money): #użycie tylko jak drużyna ma pytanie i chce kupić podpowiedź
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
    if get_hint_for_competitor(db, team) > 0:
        try:
            with db.session.begin_nested():
                substract_hint_from_competitor(db, team)
            db.session.commit()
            return {'message': 'Hint used successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
    try:
        with db.session.begin_nested():
            subtrack(db, team, money)
            add_hint_to_competitor(db, team)
        db.session.commit()
        return {'message': 'Hint bought successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400