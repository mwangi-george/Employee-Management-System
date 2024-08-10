from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.schemas import *
from app.services import EmployeeService
from models import get_db


def create_employee_routes() -> APIRouter:
    """ Creates routes for all employees endpoints"""

    # instantiate router
    router = APIRouter(prefix="/employees")

    # instantiate db operation methods
    employee_service = EmployeeService()

    # -------Add a new employee ---------#
    @router.post('/new/', response_model=ActionConfirm, status_code=status.HTTP_201_CREATED)
    async def create_employee(details: CreateEmployee, db: Session = Depends(get_db)):
        """ Creates a new employee and returns a success or failure message"""
        msg = employee_service.create_employee(employee=details, db=db)
        msg_formatted = ActionConfirm(message=msg)
        return msg_formatted

    # -------- Display employee details by -----------#
    @router.get('/profile/{id}/', response_model=EmployeeProfile, status_code=status.HTTP_200_OK)
    async def get_employee_profile(employee_id: int, db: Session = Depends(get_db)):
        """ GET details about a specific employee by their id"""
        employee_details = employee_service.get_employee_details(emp_id=employee_id, db=db)
        return employee_details

    # -------- GET all employees records within a specified range ------ #
    @router.get('/all/', response_model=MultipleEmployees, status_code=status.HTTP_200_OK)
    async def get_all_employees(start: int = 0, limit: int = 50, db: Session = Depends(get_db)):
        """ GET all employees within specified range"""
        employees = employee_service.get_all_employees(start=start, limit=limit, db=db)

        # formatted responses to conform to required schema
        employees_formatted = MultipleEmployees(employees=employees)
        return employees_formatted

    # ------ UPDATE an employees profile ---------- #
    @router.put('/profile/{id}/', response_model=ActionConfirm, status_code=status.HTTP_200_OK)
    async def update_employee_profile(employee_id: int, details: UpdateEmployee, db: Session = Depends(get_db)):
        """ Update a employee profile"""
        msg = employee_service.update_employee(emp_id=employee_id, employee=details, db=db)
        msg_formatted = ActionConfirm(message=msg)
        return msg_formatted

    # --------- UPDATE an employees position or salary ------- #
    @router.put('/profile/promote/{id}/', response_model=ActionConfirm, status_code=status.HTTP_200_OK)
    async def promote_or_demote_employee(
            employee_id: int, details: PromoteOrDemoteEmployee, db: Session = Depends(get_db)
    ):
        """ Promote or demote employee by their id"""
        msg = employee_service.promote_or_demote_employee(emp_id=employee_id, details=details, db=db)
        msg_formatted = ActionConfirm(message=msg)
        return msg_formatted

    return router
