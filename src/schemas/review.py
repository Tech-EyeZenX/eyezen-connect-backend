from pydantic import BaseModel
from datetime import datetime
from enum import Enum 
from typing import Optional 


class ReviewType(str,Enum):
    doctor = "doctor"
    shop  = "shop"

class ReviewBase(BaseModel):
    patient_id: int 
    rating: int 
    review_type: ReviewType

class ReviewCreate(ReviewBase):
    comment: Optional[str] = None 
    shop_id: Optional[str] = None 
    doctor_id: Optional[str] = None 

class Review(ReviewBase):
    id: int
    comment:Optional[str] = None
    shop_id: Optional[int] = None
    doctor_id: Optional[int]  = None
    created_at : datetime

    class Config:
        from_attributes = True

        