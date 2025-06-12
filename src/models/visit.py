from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from .base import Base

class Visit(Base):
    __tablename__ = "visit"
    
    patient_id = Column(Integer, ForeignKey("patient.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    visit_time = Column(TIMESTAMP)
    reason = Column(String)
    notes = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())