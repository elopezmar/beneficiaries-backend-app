from flask import Blueprint
from flask_restful import Api

from routes.employee.resources import CreateEmployee, Employee, EmployeeList

employee_bp = Blueprint("employee", __name__)
api = Api(employee_bp)

api.add_resource(CreateEmployee, "/employee")
api.add_resource(Employee, "/employee/<int:employee_id>")
api.add_resource(EmployeeList, "/employees")
