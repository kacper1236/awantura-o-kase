from flask import Blueprint
from database import Competitor
from database.Entity.competitor import get_competitor_money, change_game, change_bidded
from extentions import db

team_bp = Blueprint('team', __name__)

@team_bp.route("/<team>-info", methods=['GET'])
def team_info_route(team):
    competitors = Competitor.query.filter_by(name=team).one_or_none()
    if competitors:
        return { 
            "name": competitors.name,
            "money": competitors.money,
            "temp_money": competitors.temp_money,
            "bidded": competitors.bidded,
            "onevsone": competitors.onevsone,
            'lost_player': competitors.lost_player,
            'is_playing': competitors.is_playing,
            'max_bet': competitors.max_bet,
            'hint': competitors.hint
        }

    return {'error': 'Team not found'}, 404

@team_bp.route('/get-money/<team>', methods=['GET'])
def get_money_route(team):
    try:
        money = get_competitor_money(db, team)
        return {'money': money}, 200
    except Exception as e:
        return {'error': str(e)}, 400
    
@team_bp.route('/change-game/<team>', methods=['POST'])
def change_game_route(team):
    try:
        change_game(db, team)
        return {'message': f'Game status changed for {team}'}, 200
    except Exception as e:
        return {'error': str(e)}, 400
    
@team_bp.route('/change-bidded/<team>', methods=['POST'])
def change_bidded_route(team):
    try:
        change_bidded(db, team)
        return {'message': f'Bidding status changed for {team}'}, 200
    except Exception as e:
        return {'error': str(e)}, 400