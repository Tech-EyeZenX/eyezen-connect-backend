from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EvaluationBase(BaseModel):
    exam_id: int
    doctor_id : int 
    diagnosis_id : int 


class EvaluationCreate(EvaluationBase):
    clinical_notes = Optional[str]  = None
    impression: Optional[str] = None 
    management_plan: Optional[str] = None
    patient_advice: Optional[str] = None
    report_file: Optional[str] = None


class Evaluation(EvaluationBase):
    id: int
    clinical_notes : Optional[str] = None
    impression: Optional[str] = None
    management_plan: Optional[str] = None
    patient_advice: Optional[str] = None
    report_file: Optional[str] = None
    created_at : datetime 

    class Config:
        from_attributes  = True