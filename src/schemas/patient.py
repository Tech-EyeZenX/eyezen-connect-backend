from pydantic import BaseModel
from datetime import datetime 


class PaymentBase(BaseModel):
    shop_id : int 
    amount: float 
    payment_method: str 
    status:str 

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    created_at : datetime 

    class Config:
        from_attributes = True