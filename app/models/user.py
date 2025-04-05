from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String , List
from sqlalchemy.orm import relationship
from sqlalchemy import enum as sql_alchemy_enum
from enum import Enum
from app.models.payment import Payment
from typing import Optional , List


class UserRole(str, Enum):
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True)
    fname : Mapped[str] = mapped_column(String(30))
    lname : Mapped[Optional[str]] = mapped_column(String(30))
    email : Mapped[str] = mapped_column(String(100))
    role  : Mapped[UserRole] = mapped_column(sql_alchemy_enum(UserRole), default = UserRole.CUSTOMER)
    password : Mapped[str] = mapped_column(String(100))
    payments : Mapped[Optional[List[Payment]]] = relationship(backpopulates="initiator", cascade="all, delete-orphan")

