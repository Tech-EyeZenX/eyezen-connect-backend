from sqlalchemy import Column, String, Integer, TIMESTAMP, ARRAY
from .base import Base

class Doctor(Base):
    __tablename__ = "doctor"

    name = Column(String)
    email = Column(String, unique = True , index = True)
    phone = Column(String)
    registration_number = Column(String)
    specialty = Column(String)
    experience = Column(Integer)
    availability = Column(String)
    rating  = Column(Integer)
    profile_pic = Column(String)
    qualifications = Column(ARRAY(String))
    created_at = Column(TIMESTAMP)

    