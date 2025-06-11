#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
from models import Base


class BankDeposits(Base):
    """model for a table that stores deposits from bank accounts"""

    __tablename__ = "bank_deposits"

    id = Column(Integer, primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, id, amount, date):
        self.id = id
        self.amount = amount
        self.date = date
