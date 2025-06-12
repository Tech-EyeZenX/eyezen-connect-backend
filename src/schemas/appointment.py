from pydantic import BaseModel
from datetime import datetime , timedelta
from enum import Enum
from typing import Optional


class AppointmentStatus(str, Enum):
    confirmed = "confirmed"
    cancelled = "cancelled"
    completed = "completed"


class AppointmentBase(BaseModel):
    patient_id : int
    doctor_id : int
    shop_id : int
    scheduled_time : datetime
    duration : timedelta
    status : AppointmentStatus


class AppointmentCreate(AppointmentBase):
    notes: Optional[str] = None

class Appointment(AppointmentBase):
    id : int
    notes : Optional[str] = None
    created_at : datetime
    updated_at : datetime 

    class Config:
        from_attributes = True