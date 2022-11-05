from flask import Blueprint
from flask_restful import Api

from routes.nationality.resources import NationalityList

nationality_bp = Blueprint("nationality", __name__)
api = Api(nationality_bp)

api.add_resource(NationalityList, "/nationalities")
