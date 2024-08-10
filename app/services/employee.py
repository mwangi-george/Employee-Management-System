from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models import Employee
from app.schemas import CreateEmployee


class EmployeeService:
    """ Define backend db services to support all employees endpoints"""
    def __init__(self):
        """ Initialize the backend db services """
        pass

    # --------- POST a new employee to db ---------- #
    @staticmethod
    def create_employee(employee: CreateEmployee, db: Session):
        """ Create a new employee """

        # collect the employee details
        employee_details = Employee(
            name=employee.name,
            email=employee.email,
            phone=employee.phone,
            address=employee.address,
            position=employee.position,
            salary=employee.salary
        )

        # Check whether the email passed exists in the database
        db_employee = db.query(Employee).filter_by(email=employee_details.email).first()

        # raise an exception if it exists already
        if db_employee:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail='Employee already exists'
            )
        try:
            # add employee to db
            db.add(employee_details)
            db.commit()
            db.refresh(employee_details)
            return f"{employee_details.name} created successfully with id: {employee_details.id}"
        except Exception as e:
            print(f"An error occurred while creating employee {e}")
            # raise exception if operation fails
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Could not add employee"
            )

    # ---------GET employee by id ----------- #
    @staticmethod
    def get_employee_details(emp_id: int, db: Session):
        """ Get employee details from db by employee id """
        db_employee = db.query(Employee).filter_by(id=emp_id).first()
        if db_employee:
            return db_employee
        # raise a 404 error if none exists
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {emp_id} does not exist"
        )

    # -------- GET all employee records ------- #
    @staticmethod
    def get_all_employees(*, start: int = 0, limit: int = 50, db: Session):
        """ Get all employees within the specified range """
        db_employees = db.query(Employee).offset(start).limit(limit).all()
        return db_employees



