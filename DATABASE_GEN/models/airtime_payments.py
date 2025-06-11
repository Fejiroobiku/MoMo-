#!/usr/bin/python3

from models import Base
from models.payments_base import PaymentBase


class AirTime(Base, PaymentBase):
    """model for a table that stores payment to purchasing airtime"""

    __tablename__ = "airtime_payments"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
