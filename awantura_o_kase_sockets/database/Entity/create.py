from ..database import Competitor, Round, Pool, Category
import json

def create_competitors(db):
    if not Competitor.query.first():
        db.session.add(Competitor(name="niebiescy", money=5000, temp_money=0, bidded=False, onevsone=False, lost_player=False, is_playing=True, max_bet = 0, hint = 0))
        db.session.add(Competitor(name="zieloni", money=5000, temp_money=0, bidded=False, onevsone=False, lost_player=False, is_playing=True, max_bet = 0, hint = 0))
        db.session.add(Competitor(name="zolci", money=5000, temp_money=0, bidded=False, onevsone=False, lost_player=False, is_playing=True, max_bet = 0, hint = 0))
        db.session.add(Competitor(name="mistrzowie", money=5000, temp_money=0, bidded=False, onevsone=False, lost_player=False, is_playing=True, max_bet = 0, hint = 0))
        db.session.commit()

def create_rounds(db):
    if not Round.query.first():
        db.session.add(Round(round=0, bid=False, next_round=False, biggest_bid=0, is_bidding=False))
        db.session.commit()

def create_pool(db):
    if not Pool.query.first():
        db.session.add(Pool(pool=0, team=""))
        db.session.commit()

def create_category(db):
    if not Category.query.first():
        db.session.add(Category(category="Geografia", question="Jakie jest stolica Polski?", answer="Warszawa", hint=json.dumps(["To największe miasto w Polsce.", "Znajduje się nad Wisłą."])))
        db.session.add(Category(category="Matematyka", question="Ile to jest 2 + 2?", answer="4", hint=json.dumps(["To podstawowe działanie matematyczne.", "Wynik jest liczbą parzystą."])))
        db.session.commit()