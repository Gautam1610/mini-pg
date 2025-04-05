from app.models.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import enum as sql_alchemy_enum
from sqlalchemy import Float
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import ForeignKey
from app.models.user import User
from enum import Enum
from typing import Optional


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    INR = "INR"
    GBP = "GBP"
    JPY = "JPY"

class Payment(Base):
    __tablename__ = "payment_detail"

    id : Mapped[int] = mapped_column(primary_key=True)
    amount : Mapped[float] = mapped_column(Float)
    currency : Mapped[Currency] = mapped_column-(sql_alchemy_enum(Currency), default = Currency.INR)
    initiator_id : Mapped[int] = relationship(ForeignKey("users.id"))
    initiator : Mapped[User] = relationship(backpopulates="payments")

