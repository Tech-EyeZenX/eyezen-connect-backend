from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey, Enum

from sqlalchemy.sql import func

from .base import Base
from enum import Enum as PyEnum

class ReviewType(PyEnum):
    DOCTOR = "doctor"
    SHOP = "shop"

class Review(Base):
    __tablename__  = "review"
    patient_id = Column(Integer, ForeignKey("patient.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    rating  = Column(Integer)
    comment = Column(Text)
    review_type = Column(Enum(ReviewType))
    created_at = Column(TIMESTAMP, server_default = func.now())
    