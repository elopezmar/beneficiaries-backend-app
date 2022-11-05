from datetime import date
from sqlalchemy.engine.cursor import CursorResult

from services.database.session import session
from services.exceptions.procedure import ProcedureException


class Procedure:
    def __init__(self, name: str):
        self.name = name
        self.session = session

    def execute(self, **params) -> CursorResult:
        cmd = f"EXEC {self.name}"

        for k, v in params.items():
            if v is None:
                cmd = f"{cmd} @{k} = NULL,"
            elif isinstance(v, str) or isinstance(v, date):
                cmd = f"{cmd} @{k} = '{v}',"
            elif isinstance(v, bool):
                cmd = f"{cmd} @{k} = {1 if v else 0}"
            else:
                cmd = f"{cmd} @{k} = {v},"

        if cmd[-1] == ",":
            cmd = f"{cmd[:-1]};"
        else:
            cmd = f"{cmd};"

        try:
            return self.session.execute(cmd)
        except Exception as err:
            raise ProcedureException(message=str(err))

    def commit(self) -> None:
        self.session.commit()
