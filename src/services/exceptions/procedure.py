from services.exceptions.base import ApiException


class ProcedureException(ApiException):
    status_code = 500
    message = "Procedure exception"
