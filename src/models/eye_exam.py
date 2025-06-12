from sqlalchemy import Column, Integer, String, TIMESTAMP, String, ForeignKey, JSON
from sqlalchemy.sql import func
from .base import Base


class EyeExam(Base):
    __tablename__ = "eye_exam"

    patient_id = Column(Integer, ForeignKey("patient.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    shop_id = Column(Integer, ForeignKey("optical_shop.id"))
    exam_time = Column(TIMESTAMP)
    visual_acuity = Column(String)
    intraocular_pressure = Column(JSON)
    fundus_image = Column(String)
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default = func.now())