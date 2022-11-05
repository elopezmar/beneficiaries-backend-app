from flask import request
from flask_jwt import jwt_required

from services.resources.custom_resource import CustomResource
from models.beneficiary import Beneficiary as BeneficiaryModel
from validators.beneficiary import Beneficiary as BeneficiaryValidator
from validators.beneficiary import PARTIAL


class CreateBeneficiary(CustomResource):
    @jwt_required()
    def post(self, employee_id: int):
        validator = BeneficiaryValidator()
        beneficiary: BeneficiaryModel = validator.load(request.json)
        return validator.dump(beneficiary.create(employee_id))


class Beneficiary(CustomResource):
    @jwt_required()
    def put(self, employee_id: int, beneficiary_id: int):
        validator = BeneficiaryValidator()
        beneficiary = BeneficiaryModel.get(employee_id, beneficiary_id)
        return validator.dump(
            beneficiary.update(validator.load(request.json, partial=PARTIAL))
        )

    @jwt_required()
    def delete(self, employee_id: int, beneficiary_id: int):
        validator = BeneficiaryValidator()
        beneficiary = BeneficiaryModel.get(employee_id, beneficiary_id)
        return validator.dump(beneficiary.delete())


class BeneficiaryList(CustomResource):
    @jwt_required()
    def get(self, employee_id: int):
        return BeneficiaryValidator(many=True).dump(BeneficiaryModel.all(employee_id))
