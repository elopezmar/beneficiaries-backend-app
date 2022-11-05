from services.exceptions.base import ApiException


class BeneficiaryNotFoundException(ApiException):
    status_code = 404
    message = "Beneficiary not found"


class BeneficiaryCouldNotBeCreatedException(ApiException):
    status_code = 500
    message = "Beneficiary could not be created"


class BeneficiaryCouldNotBeUpdatedException(ApiException):
    status_code = 500
    message = "Beneficiary could not be updated"


class BeneficiaryParticipationExceededException(ApiException):
    status_code = 400
    message = "Employee beneficiaries total participation percentage could not be more than 100%"
