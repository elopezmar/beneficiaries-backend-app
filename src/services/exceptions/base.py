class ApiException(Exception):
    status_code = 500
    message = "API Exception"

    def __init__(self, status_code: int = None, message: str = None):
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message
        super().__init__(self.message)

    def get_response(self) -> tuple:
        return {"message": self.message}, self.status_code
