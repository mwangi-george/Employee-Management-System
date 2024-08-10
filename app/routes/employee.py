from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas import (
    CreateEmployee,
    ActionConfirm,
    EmployeeProfile,
    )
from app.services import EmployeeService
from models import get_db


def create_employee_routes() -> APIRouter:
    """ Creates routes for all employees endpoints"""

    # instantiate router
    router = APIRouter(prefix="/employee")

    # instantiate db operation methods
    employee_service = EmployeeService()

    # -------Add a new employee ---------#
    @router.post('/new/', response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_employee(employee: CreateEmployee, db: Session = Depends(get_db)):
        """ Creates a new employee and returns a success or failure message"""
        msg = employee_service.create_employee(employee=employee, db=db)
        msg_formatted = ActionConfirm(message=msg)
        return msg_formatted

    # -------- Display employee details by -----------#
    @router.get('/profile/{id}/', response_model=EmployeeProfile, status_code=status.HTTP_200_OK)
    async def get_employee_profile(emp_id: int, db: Session = Depends(get_db)):
        """ GET details about a specific employee by their id"""
        employee = employee_service.get_employee_details(emp_id=emp_id, db=db)
        return employee

    return router
