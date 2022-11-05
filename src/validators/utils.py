from dateutil.relativedelta import relativedelta
from datetime import date

from services.exceptions.validators import (
    InvalidPhoneLengthException,
    InvalidPhoneNumberException,
    PersonShouldBeAnAdultException,
)


def validate_birth_date(birth_date: date):
    if relativedelta(date.today(), birth_date).years < 18:
        raise PersonShouldBeAnAdultException


def validate_phone(phone: str):
    if len(phone) != 10:
        raise InvalidPhoneLengthException

    try:
        int(phone)
    except ValueError:
        raise InvalidPhoneNumberException
