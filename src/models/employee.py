from __future__ import annotations
from copy import copy
from datetime import date
from typing import List, Optional, Union
from dataclasses import dataclass

from models.nationality import Nationality
from services.database.procedure import Procedure
from services.database.constants import (
    SP_ALL_EMPLOYEES,
    SP_GET_EMPLOYEE,
    SP_INSERT_EMPLOYEE,
    SP_UPDATE_EMPLOYEE,
)
from services.exceptions.employee import (
    EmployeeCouldNotBeCreatedException,
    EmployeeCouldNotBeUpdatedException,
    EmployeeNotFoundException,
)
from validators.utils import validate_birth_date, validate_phone


@dataclass
class Employee:
    id: Optional[int] = None
    nationality_id: Optional[int] = None
    nationality: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[Union[date, str]] = None
    employee_number: Optional[str] = None
    curp: Optional[str] = None
    ssn: Optional[str] = None
    phone: Optional[str] = None
    is_active: Optional[Union[bool, int]] = True

    def __post_init__(self):
        if self.curp and len(self.curp) == 0:
            self.curp = None
        if self.ssn and len(self.ssn) == 0:
            self.ssn = None
        if isinstance(self.birth_date, str):
            self.birth_date = date.fromisoformat(self.birth_date)
        if isinstance(self.is_active, int):
            self.is_active = self.is_active == 1

    @classmethod
    def all(cls) -> List[Employee]:
        procedure = Procedure(SP_ALL_EMPLOYEES)
        results: List[Employee] = []

        for row in procedure.execute():
            results.append(Employee(**row._mapping))

        return results

    @classmethod
    def get(cls, id: int) -> Employee:
        procedure = Procedure(SP_GET_EMPLOYEE)

        for row in procedure.execute(id=id):
            return Employee(**row._mapping)

        raise EmployeeNotFoundException(message=f"Employee not found for id {id}")

    def create(self) -> Employee:
        validate_birth_date(self.birth_date)
        validate_phone(self.phone)

        nationality = Nationality.get(self.nationality_id)

        procedure = Procedure(SP_INSERT_EMPLOYEE)
        params = copy(self.__dict__)
        params.pop("id", None)
        params.pop("is_active", None)
        params.pop("nationality", None)

        inserted: Optional[Employee] = None

        for row in procedure.execute(**params):
            inserted = Employee(**row._mapping, nationality=nationality.description)

        if inserted:
            procedure.commit()
            return inserted

        raise EmployeeCouldNotBeCreatedException

    def update(self, to_update: Employee) -> Employee:
        nationality: Optional[Nationality] = None

        if to_update.birth_date is not None:
            validate_birth_date(to_update.birth_date)
        if to_update.phone is not None:
            validate_phone(to_update.phone)
        if to_update.nationality_id is not None:
            nationality = Nationality.get(to_update.nationality_id)

        for k, v in to_update.__dict__.items():
            if v is None:
                continue
            self.__setattr__(k, v)

        procedure = Procedure(SP_UPDATE_EMPLOYEE)
        params = copy(self.__dict__)
        params.pop("nationality", None)
        updated: Optional[Employee] = None

        for row in procedure.execute(**params):
            updated = Employee(
                **row._mapping,
                nationality=nationality.description if nationality else None,
            )

        if updated:
            procedure.commit()
            return updated

        raise EmployeeCouldNotBeUpdatedException

    def delete(self) -> Employee:
        to_update = Employee(is_active=False)
        return self.update(to_update)
