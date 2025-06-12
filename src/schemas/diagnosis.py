from pydantic import BaseModel
from typing import Dict, List, Optional

class DiagnosisBase(BaseModel):
    test_name : str
    description : str
    doctor_id : int 
    patient_id : int
    affected_eye : str

class DiagnosisCreate(DiagnosisBase):
    known_conditions : Optional[List[str]]  = None
    medical_history : Optional[str] = None

class Diagnosis(DiagnosisBase):
    id: int
    known_conditions: Optional[List[str]] = None
    medical_history: Optional[str] = None

    class Config:
        from_attributes = True

    
