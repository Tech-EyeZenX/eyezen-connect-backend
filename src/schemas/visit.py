from pydantic import BaseModel
from datetime import datetime
from typing import Optional
class VisitBase(BaseModel):
    patient_id : int
    doctor_id : int
    shop_id : int
    visit_time : datetime
    reason:str


class VisitCreate(VisitBase):
    notes: Optional[str] = None 


class Visit(VisitBase):
    id: int
    notes: Optional[str] = None 
    created_at : datetime 


    class Config:
        from_attributes = True