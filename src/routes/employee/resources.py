from flask import request

from flask_jwt import jwt_required
from services.resources.custom_resource import CustomResource
from models.employee import Employee as EmployeeModel
from validators.employee import Employee as EmployeeValidator
from validators.employee import PARTIAL


class CreateEmployee(CustomResource):
    @jwt_required()
    def post(self):
        validator = EmployeeValidator()
        employee: EmployeeModel = validator.load(request.json)
        return validator.dump(employee.create())


class Employee(CustomResource):
    @jwt_required()
    def get(self, employee_id: int):
        return EmployeeValidator().dump(EmployeeModel.get(employee_id))

    @jwt_required()
    def put(self, employee_id: int):
        validator = EmployeeValidator()
        employee = EmployeeModel.get(employee_id)
        return validator.dump(
            employee.update(validator.load(request.json, partial=PARTIAL))
        )

    @jwt_required()
    def delete(self, employee_id: int):
        validator = EmployeeValidator()
        employee = EmployeeModel.get(employee_id)
        return validator.dump(employee.delete())


class EmployeeList(CustomResource):
    @jwt_required()
    def get(self):
        return EmployeeValidator(many=True).dump(EmployeeModel.all())
