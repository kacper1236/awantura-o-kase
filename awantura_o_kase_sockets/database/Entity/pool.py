from ..database import Pool, Competitor

def add_pool(db, team, money):
    pool = db.session.query(Pool).first()
    teams = db.session.query(Competitor).filter_by(name = team).first()
    max_temp_money = max(comp.temp_money for comp in db.session.query(Competitor).all())
    max_bid = max(comp.max_bet for comp in db.session.query(Competitor).all())
    if money <= max_bid:
        raise ValueError("Money cannot be less than the maximum temporary money of any team.")

    if pool:
        print(money - max_temp_money)
        pool.pool += (money - max_temp_money)
        pool.team = team
        teams.max_bid = money
    else:
        new_pool = Pool(pool=money, team=team)
        db.session.add(new_pool) 

def get_pool(db):
    pool = db.session.query(Pool.pool, Pool.team).first()
    if not pool:
        return None
    return {"pool": pool.pool, "team": pool.team} 

def reset_pool(db):
    pool = db.session.query(Pool).first()
    pool.pool = 0
    pool.team = ""
    db.session.commit()

def assign_pool_for_new_round(db):
    pool = db.session.query(Pool).first()
    if pool:
        pool.pool = 600
        pool.team = ""
    else:
        new_pool = Pool(pool=600, team="")
        db.session.add(new_pool)
