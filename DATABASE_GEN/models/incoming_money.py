#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
from models import Base


class IncomingMoney(Base):
    """model for a table that stores amount recieved"""

    __tablename__ = "money_recieved"

    # date in millliseconds will serve as our unique id
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, id, first_name, last_name, amount, date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount
        self.date = date
