from sqlalchemy import Column, Integer, ForeignKey
from .base import Base


class PatientDoctor(Base):
    __tablename__  = "patient_doctor"
    patient_id = Column(Integer, ForeignKey("patient.id"),primary_key = True)
    doctor_id = Column(Integer, ForeignKey("doctor.id"), primary_key = True)