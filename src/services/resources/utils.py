import functools
from marshmallow import ValidationError
from flask_jwt import JWTError

from services.exceptions.base import ApiException


def handle_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as err:
            return err.messages, 400
        except ApiException as err:
            return err.get_response()
        except JWTError as err:
            return ApiException(status_code=401, message=str(err)).get_response()
        except Exception as err:
            return ApiException(
                status_code=500, message=f"An error ocurred: {str(err)}"
            )

    return wrapper
