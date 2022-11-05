from marshmallow import fields
from marshmallow.validate import Length

from services.validators.dataclass_schema import DataclassSchema
from models.employee import Employee as EmployeeModel

PARTIAL = (
    "nationality_id",
    "first_name",
    "last_name",
    "birth_date",
    "employee_number",
    "phone",
)


class Employee(DataclassSchema):
    __model__ = EmployeeModel

    id = fields.Integer()
    nationality_id = fields.Integer(required=True, data_key="nationalityId")
    nationality = fields.String()
    first_name = fields.String(
        required=True, data_key="firstName", validate=Length(0, 50)
    )
    last_name = fields.String(
        required=True, data_key="lastName", validate=Length(0, 50)
    )
    birth_date = fields.Date(required=True, data_key="birthDate")
    employee_number = fields.String(
        required=True, data_key="employeeNumber", validate=Length(0, 10)
    )
    curp = fields.String(validate=Length(0, 18))
    ssn = fields.String(validate=Length(0, 9))
    phone = fields.String(required=True)
    is_active = fields.Boolean(data_key="isActive")
