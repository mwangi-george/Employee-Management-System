from pydantic import BaseModel, EmailStr, Field


class ActionConfirm(BaseModel):
    """ Creates a success or failure action message to show as API call response """
    message: str


class CreateEmployee(BaseModel):
    """ Creates a valid Employee object to post to DB """
    name: str
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=25)
    address: str
    position: str
    salary: int

    class Config:
        from_attributes = True
        # An Example schema for swagger documentation
        json_schema_extra = {
            "example": {
                "name": "Patrick K. James",
                "email": "patrick_james@fastland.com",
                "phone": "+254-749-555-555",
                "address": "12th Avenue, Kahawa Estate",
                "position": "Senior Systems Engineer",
                "salary": 2000000,
            }
        }


class EmployeeProfile(BaseModel):
    """ Creates a valid Employee response object"""
    id: int
    name: str
    email: str
    phone: str
    address: str
    position: str
    salary: int

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "<NAME>",
                "email": "<EMAIL>",
                "phone": "+254-749-555-555",
                "address": "12th Avenue, Kahawa Estate",
                "position": "Senior Systems Engineer",
                "salary": 2000000,
            }
        }


class MultipleEmployees(BaseModel):
    """ Returns a list of Employee objects """
    employees: list[EmployeeProfile]
