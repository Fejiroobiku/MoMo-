#!/usr/bin/python3
from models import Base
from models.payments_base import PaymentBase


class Bundles(Base, PaymentBase):
    """model for a table that stores payment to buying bundles"""

    __tablename__ = "bundles_and_packs"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
