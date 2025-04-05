from pydantic import BaseModel
from typing import Optional
from app.models.payment import Currency
from enum import Enum


class PaymentCreate(BaseModel):
    amount : float
    currency : Currency
    initiator_id : int

class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class PaymentResponse(BaseModel):
    id : int
    amount : float
    currency : str
    initiator_id : int
    status : PaymentStatus
