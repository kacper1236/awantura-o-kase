from flask import Blueprint
from database.Entity.round import *
from database.Entity.pool import *
from database.Entity.competitor import *
from extentions import db

game_bp = Blueprint('game', __name__)

@game_bp.route("/reset-game", methods=['POST'])
def reset_game_route():
    global_reset_round(db)
    reset_pool(db)
    reset_competitors(db)
    return {'message': 'Game reset successfully'}, 200

@game_bp.route('/add-pool/<team>/<int:money>', methods=['POST'])
def add_to_pool_route(team, money):
    if not isinstance(money, int):
        return {'error': 'Money must be an integer'}, 400
    if money <= 0:
        return {'error': 'Money cannot be negative'}, 400
    if not team:
        return {'error': 'Team name cannot be empty'}, 400
    if not is_playing(db, team):
        return {'error': f'Team {team} is not playing'}, 400
    if is_bidded(db, team):
        return {'error': f'Team {team} has already bidded'}, 400
    if not is_competitors_bidding(db):
        return {'error': 'Round is not bidding. Competitors cannot add to pool.'}, 400
    try:
        with db.session.begin_nested():
            add_pool(db, team, money)
            subtrack(db, team, money)
            add_temp_money(db, team, money)
            maximize_bet(db, team, money)
            change_bidded(db, team)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
    return {'message': f'Added {money} to {team} pool'}, 200
    
@game_bp.route('/reset-temp-money', methods=['POST'])
def reset_temp_money_route():
    try:
        reset_temp_money(db)
        return {'message': f'Reset temporary money'}, 200
    except Exception as e:
        return {'error': str(e)}, 400

