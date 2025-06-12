from sqlalchemy import Column, Integer, String, Numeric, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from .base import Base

class AIAnalysis(Base):
    __tablename__ = "ai_analysis"
    exam_id = Column(Integer, ForeignKey("eye_exam.id"))
    model_version = Column(String)
    clinical_report = Column(String)
    retinal_feature_extraction = Column(String)
    Microaneurysm_detection = Column(String)
    findings = Column(JSON)
    confidence_score = Column(Numeric)
    generated_at = Column(TIMESTAMP, server_default = func.now())
