from pydantic import BaseModel
from datetime import datetime 
from typing import Dict, List, Optional


class EyeExamBase(BaseModel):
    patient_id : int
    doctor_id: int
    shop_id:  int 
    exam_time : datetime 
    status: str


class EyeExamCreate(EyeExamBase):
    visual_acuity: Optional[Dict] = None
    intraocular_pressure : Optional[Dict] = None
    fundus_image: Optional[List[str]] = None

class EyeExam(EyeExamBase):
    id : int
    visual_acuity: Optional[Dict] = None
    intraocular_pressure : Optional[Dict] = None
    fundus_image: Optional[List[str]] = None

    class Config:
        from_attributes = True