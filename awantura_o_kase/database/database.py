from extentions import db
from sqlalchemy.orm import Mapped
from typing import List

class Competitor(db.Model):
    __tablename__ = 'competitor'

    name: Mapped[str] = db.Column(db.String(30), primary_key=True, nullable=False)
    money: Mapped[int] = db.Column(db.Integer, nullable=False)
    temp_money: Mapped[int] = db.Column(db.Integer, nullable=False)
    bidded: Mapped[bool] = db.Column(db.Boolean, nullable=False)
    onevsone: Mapped[bool] = db.Column(db.Boolean, nullable=False)
    lost_player: Mapped[bool] = db.Column(db.Boolean, nullable=False, default=False)
    is_playing: Mapped[bool] = db.Column(db.Boolean, nullable=False, default=True)
    max_bet: Mapped[int] = db.Column(db.Integer, nullable=False, default=0)
    hint: Mapped[int] = db.Column(db.Integer, nullable=False, default=0)
    blackbox: Mapped[int] = db.Column(db.Integer, nullable=False, default=0)

class Category(db.Model):
    __tablename__ = 'category'

    category: Mapped[str] = db.Column(db.String(300), primary_key=True, nullable=False)
    question: Mapped[str] = db.Column(db.String(3000), nullable=False)
    answer: Mapped[str] = db.Column(db.String(3000), nullable=False)
    hint: Mapped[List[str]] = db.Column(db.String(), nullable=False)

class Round(db.Model):
    __tablename__ = 'round'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    round: Mapped[int] = db.Column(db.Integer, nullable=False)
    bid: Mapped[bool] = db.Column(db.Boolean, nullable=False)
    next_round: Mapped[bool] = db.Column(db.Boolean, nullable=False)
    biggest_bid: Mapped[int] = db.Column(db.Integer, nullable=False)
    is_bidding: Mapped[bool] = db.Column(db.Boolean, nullable=False, default=False)

class Pool(db.Model):
    __tablename__ = 'pool'

    id: Mapped[int] = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pool: Mapped[int] = db.Column(db.Integer, nullable=False)
    team: Mapped[str] = db.Column(db.String(30), nullable=False)

