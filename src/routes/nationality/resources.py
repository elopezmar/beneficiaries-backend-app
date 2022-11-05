from flask_jwt import jwt_required
from services.resources.custom_resource import CustomResource
from models.nationality import Nationality as NationalityModel
from validators.nationality import Nationality as NationalityValidator


class NationalityList(CustomResource):
    @jwt_required()
    def get(self):
        return NationalityValidator(many=True).dump(NationalityModel.all())
