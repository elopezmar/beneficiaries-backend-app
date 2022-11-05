from flask import Blueprint
from flask_restful import Api

from routes.beneficiary.resources import CreateBeneficiary, Beneficiary, BeneficiaryList

beneficiary_bp = Blueprint("beneficiary", __name__)
api = Api(beneficiary_bp, prefix="/employee/<int:employee_id>")

api.add_resource(CreateBeneficiary, "/beneficiary")
api.add_resource(Beneficiary, "/beneficiary/<int:beneficiary_id>")
api.add_resource(BeneficiaryList, "/beneficiaries")
