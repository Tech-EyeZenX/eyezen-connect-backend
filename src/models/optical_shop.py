from sqlalchemy import Column, String, Numeric, TIMESTAMP 
from .base import Base


class OpticalShop(Base):
    __tablename__ = "optical_shop"

    email = Column(String, unique = True, index = True)
    shop_name = Column(String)
    locale = Column(String)
    optometrist_name = Column(String)
    phone_number = Column(String)
    password = Column(String)
    address = Column(String)
    profile_pic = Column(String)
    license_number = Column(String)
    registration_number = Column(String)
    working_hours = Column(String)
    rating = Column(Numeric)
    website_url = Column(String)
    created_at = Column(TIMESTAMP)
    last_login = Column(TIMESTAMP)