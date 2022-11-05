from marshmallow import fields
from marshmallow.validate import Length

from services.validators.dataclass_schema import DataclassSchema
from models.beneficiary import Beneficiary as BeneficiaryModel

PARTIAL = (
    "nationality_id",
    "first_name",
    "last_name",
    "birth_date",
    "phone",
    "participation_percent",
)


class Beneficiary(DataclassSchema):
    __model__ = BeneficiaryModel

    id = fields.Integer()
    nationality_id = fields.Integer(required=True, data_key="nationalityId")
    nationality = fields.String()
    employee_id = fields.Integer(dump_only=True, data_key="employeeId")
    first_name = fields.String(
        required=True, data_key="firstName", validate=Length(0, 50)
    )
    last_name = fields.String(
        required=True, data_key="lastName", validate=Length(0, 50)
    )
    birth_date = fields.Date(required=True, data_key="birthDate")
    curp = fields.String(validate=Length(0, 18))
    ssn = fields.String(validate=Length(0, 9))
    phone = fields.String(required=True, validate=Length(0, 10))
    participation_percent = fields.Float(required=True, data_key="participationPercent")
    is_active = fields.Boolean(data_key="isActive")
