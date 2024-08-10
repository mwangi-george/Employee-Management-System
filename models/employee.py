from sqlalchemy import Column, Integer, String
from .base import Base


class Employee(Base):
    """Employee data model"""
    __tablename__ = 'employees'

    # fields
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary = Column(Integer, nullable=False)
