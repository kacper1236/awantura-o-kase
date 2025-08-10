from ..database import Competitor

def subtrack(db, team, money):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    max_temp_money = max(comp.temp_money for comp in db.session.query(Competitor).all())
    if max_temp_money > money:
        raise ValueError(f"Temporary money {max_temp_money} exceeds the amount to subtract {money}.")
    if competitor:
        if competitor.money >= money:
            competitor.money -= (money - competitor.temp_money)
        else:
            raise ValueError(f"Not enough money for {team}. Current balance: {competitor.money}, attempted deduction: {money}.")
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def add_money(db, team, money):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.money += money
    else:
        raise ValueError(f"Competitor {team} not found in the database.")

def add_temp_money(db, team, money):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.temp_money += money - competitor.temp_money
    else:
        raise ValueError(f"Competitor {team} not found in the database.")

def assing_temp_money(db, team, money):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.temp_money = money
    else:
        raise ValueError(f"Competitor {team} not found in the database.")

def reset_temp_money(db, team):
    competitor = db.session.query(Competitor).all()
    try:
        for comp in competitor:
            if comp.name == team:
                comp.temp_money = 0
        db.session.commit()
    except:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def reset_temp_money_all(db):
    competitor = db.session.query(Competitor).all()
    for comp in competitor:
        comp.temp_money = 0
    db.session.commit()

def get_competitor_money(db, team):
    competitor = db.session.query(Competitor.money).filter_by(name = team).first()
    if competitor:
        return competitor.money
    else:
        raise ValueError(f"Competitor {team} not found in the database.")

def change_game(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.is_playing = not competitor.is_playing
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def change_bidded(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.bidded = not competitor.bidded
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def change_onevsone(db, team:list[str]):
    for i in team:
        competitor = db.session.query(Competitor).filter_by(name = i).first()
        if competitor:
            competitor.onevsone = not competitor.onevsone
        else:
            raise ValueError(f"Competitor {team} not found in the database.")
        
def reset_onevsone(db):
    competitors = db.session.query(Competitor).all()
    for competitor in competitors:
        competitor.onevsone = False
    db.session.commit()
    
def reset_competitors(db):
    competitors = db.session.query(Competitor).all()
    for competitor in competitors:
        competitor.money = 5000
        competitor.temp_money = 0
        competitor.bidded = False
        competitor.onevsone = False
        competitor.lost_player = False
        competitor.is_playing = True
        competitor.max_bet = 0
        competitor.hint = 0
        competitor.blackbox = 0
    
    db.session.commit()

def is_playing(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        return competitor.is_playing
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def maximize_bet(db, team, money):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.max_bet = money
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def is_bidded(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        return competitor.bidded
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def change_lost_player(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.lost_player = not competitor.lost_player
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def is_lost_player(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        return competitor.lost_player
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
