from services.exceptions.base import ApiException


class EmployeeNotFoundException(ApiException):
    status_code = 404
    message = "Employee not found"


class EmployeeCouldNotBeCreatedException(ApiException):
    status_code = 500
    message = "Employee could not be created"


class EmployeeCouldNotBeUpdatedException(ApiException):
    status_code = 500
    message = "Employee could not be updated"
