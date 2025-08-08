from flask_socketio import emit
from database import Competitor
from database.Entity.competitor import get_competitor_money, change_game, change_bidded
from extentions import db

def register_team_socketio_handlers(socketio):
    @socketio.on('get_team_info')
    def handle_team_info(data):
        team = data.get('team')
        if not team:
            emit('error', {'error': 'Team name is required'})
            return

        competitors = Competitor.query.filter_by(name=team).one_or_none()
        if competitors:
            emit('team_info', {
                "name": competitors.name,
                "money": competitors.money,
                "temp_money": competitors.temp_money,
                "bidded": competitors.bidded,
                "onevsone": competitors.onevsone,
                'lost_player': competitors.lost_player,
                'is_playing': competitors.is_playing,
                'max_bet': competitors.max_bet,
                'hint': competitors.hint
            })
        else:
            emit('error', {'error': 'Team not found'})

    @socketio.on('get_money')
    def handle_get_money(data):
        team = data.get('team')
        if not team:
            emit('error', {'error': 'Team name is required'})
            return

        try:
            money = get_competitor_money(db, team)
            emit('team_money', {'team': team, 'money': money})
        except Exception as e:
            emit('error', {'error': str(e)})

    @socketio.on('change_game')
    def handle_change_game(data):
        team = data.get('team')
        if not team:
            emit('error', {'error': 'Team name is required'})
            return

        try:
            change_game(db, team)
            emit('game_status_changed', {'message': f'Game status changed for {team}', 'team': team}, broadcast=True)
        except Exception as e:
            emit('error', {'error': str(e)})

    @socketio.on('change_bidded')
    def handle_change_bidded(data):
        team = data.get('team')
        if not team:
            emit('error', {'error': 'Team name is required'})
            return

        try:
            change_bidded(db, team)
            emit('bidding_status_changed', {'message': f'Bidding status changed for {team}', 'team': team}, broadcast=True)
        except Exception as e:
            emit('error', {'error': str(e)})
