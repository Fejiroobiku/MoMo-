#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime
from models import Base


class PaymentToCode(Base):
    """model for a table that stores payment to codes"""

    __tablename__ = "payment_to_code"

    # date in millliseconds will serve as our unique id
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    code = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, id, first_name, last_name, code, amount, date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.code = code
        self.amount = amount
        self.date = date
