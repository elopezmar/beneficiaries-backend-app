from services.exceptions.base import ApiException


class NationalityNotFoundException(ApiException):
    status_code = 404
    message = "Nationality not found"
