from marshmallow import fields

from services.validators.dataclass_schema import DataclassSchema
from models.nationality import Nationality as NationalityModel


class Nationality(DataclassSchema):
    __model__ = NationalityModel

    id = fields.Integer()
    description = fields.String()
