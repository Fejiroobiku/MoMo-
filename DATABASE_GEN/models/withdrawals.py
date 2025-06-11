#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
from models import Base


class Withdrawals(Base):
    """model for a table that stores withdraw transactions"""

    __tablename__ = "withdrawals"
    id = Column(Integer, primary_key=True, nullable=False)
    agent = Column(String(60), nullable=False)
    agent_tel = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, id, agent, agent_tel, amount, fee, date):
        self.id = id
        self.agent = agent
        self.agent_tel = agent_tel
        self.amount = amount
        self.fee = fee
        self.date = date
