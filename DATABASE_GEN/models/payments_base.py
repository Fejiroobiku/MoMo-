#!usr/bin/python3

from sqlalchemy import Column, String, Integer, DateTime


class PaymentBase:
    """model for all payment related tables"""

    id = Column(Integer, primary_key=True, nullable=False)
    amount = Column(Integer, nullable=False)
    service_provider = Column(String(60), default="MTN", nullable=False)
    fee = Column(Integer, default=0, nullable=False)
    date = Column(DateTime, nullable=False)

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
