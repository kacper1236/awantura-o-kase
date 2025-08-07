from flask import Flask
from extentions import db

from database.Entity.create import create_competitors, create_rounds, create_pool, create_category

from routes.team_routes import team_bp
from routes.game_routes import game_bp
from routes.pool_routes import pool_bp
from routes.round_routes import round_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///awantura_o_kase.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_competitors(db)
        create_rounds(db)
        create_pool(db)
        create_category(db)

    app.register_blueprint(team_bp, url_prefix='/team')
    app.register_blueprint(game_bp, url_prefix='/game')
    app.register_blueprint(pool_bp, url_prefix='/pool')
    app.register_blueprint(round_bp, url_prefix='/round')

    return app

app = create_app()

@app.route("/")
def home():
    return "Nothing here, search for something else"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)