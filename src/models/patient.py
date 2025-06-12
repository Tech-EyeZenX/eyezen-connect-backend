from sqlalchemy import Column, String, Date, Integer, TIMESTAMP, ForeignKey
from .base import Base

class Patient(Base):
    __talbename__ = "patient"

    email = Column(String, unique = True, index = True)
    name = Column(String)
    phone = Column(String)
    date_of_birth = Column(Date)
    address = Column(String)
    gender = Column(String)
    blood_group = Column(String)
    emergency_contact_name = Column(String)
    emergency_contact_phone = Column(String)
    optical_shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    created_at = Column(TIMESTAMP)


