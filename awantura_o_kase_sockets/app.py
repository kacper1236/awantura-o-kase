from flask import Flask
from flask_socketio import SocketIO
from extentions import db
from routes.pool_routes import register_pool_socketio_handlers
from routes.game_routes import register_game_socketio_handlers
from routes.modifier_routes import register_modifier_socketio_handlers
from routes.round_routes import register_round_socketio_handlers
from routes.team_routes import register_team_socketio_handlers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # lub Twoja baza

db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# rejestrujemy WS
register_pool_socketio_handlers(socketio)
register_game_socketio_handlers(socketio)
register_modifier_socketio_handlers(socketio)
register_round_socketio_handlers(socketio)
register_team_socketio_handlers(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)
