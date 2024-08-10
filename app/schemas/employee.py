from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Employee(BaseModel):
    """ Creates a valid Employee object to post to DB """
    name: str
    email: EmailStr
    phone: PhoneNumber = Field(..., min_length=10, max_length=15)
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
