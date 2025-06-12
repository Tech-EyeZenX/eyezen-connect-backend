from sqlalchemy import Column, Integer, ForeignKey
from .base import Base 


class DoctorOpticalShop(Base):
    __tablename__ = "doctor_optical_shop"
    doctor_id = Column(Integer, ForeignKey("doctor.id"), primary_key = True)
    shop_id = Column(Integer, ForeignKey("optical_shop.id"),primary_key = True)