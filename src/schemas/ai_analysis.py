from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class AIAnalysisBase(BaseModel):
    exam_id: int
    model_version: str

class AIAnalysisCreate(AIAnalysisBase):
    clinical_report: Optional[str] = None
    retinal_feature_extraction: Optional[str] = None
    Microaneurysm_detection: Optional[str] = None
    findings: Optional[Dict] = None
    confidence_score: Optional[float] = None

class AIAnalysis(AIAnalysisBase):
    id: int
    clinical_report: Optional[str] = None
    retinal_feature_extraction: Optional[str] = None
    Microaneurysm_detection: Optional[str] = None
    findings: Optional[Dict] = None
    confidence_score: Optional[float] = None
    generated_at: datetime
    
    class Config:
        from_attributes = True