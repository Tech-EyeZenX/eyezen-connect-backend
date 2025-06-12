from sqlalchemy import Column, Integer, TIMESTAMP, Interval, String, ForeignKey, Enum
from sqlalchemy.sql import func
from .base import Base
from enum import Enum as PyEnum 

class AppointmentStatus(PyEnum):
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Appointment(Base):
    __tablename__ = "appointment"

    patient_id = Column(Integer, ForeignKey("patient.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    scheduled_time = Column(TIMESTAMP)
    duration = Column(Interval)
    notes = Column(String , nullable = True)
    status = Column(Enum(AppointmentStatus))
    created_at = Column(TIMESTAMP, server_default = func.now())
    updated_at = Column(TIMESTAMP, server_default = func.now(), onupdate = func.now())