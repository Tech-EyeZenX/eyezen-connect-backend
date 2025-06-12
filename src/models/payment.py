from sqlalchemy import Column, Integer, String, Numeric, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from .base import Base 

class Payment(Base):
    __tablename__ = "payment"

    shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    amount = Column(Numeric)
    payment_method = Column(String)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default = func.now())