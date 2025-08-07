from ..database import Round, Competitor

def reset_round(db):
    Round.query.update({
        Round.bid: False,
        Round.next_round: False,
        Round.biggest_bid: 0,
        Round.is_bidding: False
    })
    db.session.commit()

def global_reset_round(db):
    Round.query.update({
        Round.round: 0,
        Round.bid: False,
        Round.next_round: False,
        Round.biggest_bid: 0,
        Round.is_bidding: False
    })
    db.session.commit()

def next_round(db):
    current_round = db.session.query(Round).first()
    if current_round:
        current_round.round += 1
        current_round.bid = False
        current_round.next_round = False
        current_round.biggest_bid = 0
        current_round.is_bidding = True
    else:
        new_round = Round(round=1, bid=False, next_round=False, biggest_bid=0, is_bidding=False)
        db.session.add(new_round)

def take_money_to_next_round(db):
    competitors = db.session.query(Competitor).all()
    for competitor in competitors:
        competitor.money -= 200
        competitor.temp_money = 200

def get_round(db):
    round_info = db.session.query(Round).first()
    if round_info:
        return {
            "round": round_info.round,
            "bid": round_info.bid,
            "next_round": round_info.next_round,
            "biggest_bid": round_info.biggest_bid,
            "is_bidding": round_info.is_bidding
        }
    
def close_round(db):
    current_round = db.session.query(Round).first()
    if current_round:
        current_round.is_bidding = False

def open_round(db):
    current_round = db.session.query(Round).first()
    if current_round:
        current_round.is_bidding = True

def is_competitors_bidding(db):
    current_round = db.session.query(Round).first()
    if current_round:
        return current_round.is_bidding
    return False

def add_hint_to_competitor(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.hint += 1
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def get_hint_for_competitor(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        return competitor.hint
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def substract_hint_from_competitor(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.hint -= 1
    else:
        raise ValueError(f"Competitor {team} not found in the database.")

def add_blackbox_to_competitor(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        competitor.blackbox += 1
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
def get_blackbox_for_competitor(db, team):
    competitor = db.session.query(Competitor).filter_by(name = team).first()
    if competitor:
        return competitor.blackbox
    else:
        raise ValueError(f"Competitor {team} not found in the database.")
    
