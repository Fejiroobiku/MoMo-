#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
from models import Base


class TransferToMomo(Base):
    """model for a table that stores transfers to mobile numbers"""

    __tablename__ = "transfers_to_momo"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    tel = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    fee = Column(Integer, nullable=True)
    date = Column(DateTime, nullable=False)

    def __init__(self, id, first_name, last_name, tel, fee, amount, date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.amount = amount
        self.fee = fee
        self.date = date
