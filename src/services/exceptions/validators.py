from services.exceptions.base import ApiException


class PersonShouldBeAnAdultException(ApiException):
    status_code = 400
    message = "Person should be an adult"


class InvalidPhoneLengthException(ApiException):
    status_code = 400
    message = "Phone length must be 10 digits"


class InvalidPhoneNumberException(ApiException):
    status_code = 400
    message = "Only numbers are allowed for phone number"
