from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.sql import func
from .base import Base 

class Diagnosis(Base):
    __tablename__ = "diagnosis"

    test_name = Column(String)
    description = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
    affected_eye = Column(String)
    known_conditions = Column(JSON)
    medical_history = Column(String)

    