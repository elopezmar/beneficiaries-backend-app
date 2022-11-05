from __future__ import annotations
from copy import copy
from datetime import date
from decimal import Decimal
from typing import List, Optional, Union
from dataclasses import dataclass

from models.employee import Employee
from models.nationality import Nationality
from services.database.procedure import Procedure
from services.database.constants import (
    SP_ALL_BENEFICIARIES,
    SP_GET_BENEFICIARY,
    SP_INSERT_BENEFICIARY,
    SP_UPDATE_BENEFICIARY,
)
from services.exceptions.beneficiary import (
    BeneficiaryCouldNotBeCreatedException,
    BeneficiaryCouldNotBeUpdatedException,
    BeneficiaryNotFoundException,
    BeneficiaryParticipationExceededException,
)
from validators.utils import validate_birth_date, validate_phone


@dataclass
class Beneficiary:
    id: Optional[int] = None
    nationality_id: Optional[int] = None
    nationality: Optional[str] = None
    employee_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birth_date: Optional[Union[date, str]] = None
    curp: Optional[str] = None
    ssn: Optional[str] = None
    phone: Optional[str] = None
    participation_percent: Optional[float] = None
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
        if isinstance(self.participation_percent, Decimal):
            self.participation_percent = float(self.participation_percent)
        if isinstance(self.participation_percent, float):
            self.participation_percent = round(self.participation_percent, 2)

    @classmethod
    def all(cls, employee_id: int) -> List[Beneficiary]:
        procedure = Procedure(SP_ALL_BENEFICIARIES)
        results: List[Beneficiary] = []

        for row in procedure.execute(employee_id=employee_id):
            results.append(Beneficiary(**row._mapping))

        return results

    @classmethod
    def get(cls, employee_id: int, id: int) -> Beneficiary:
        procedure = Procedure(SP_GET_BENEFICIARY)

        for row in procedure.execute(id=id, employee_id=employee_id):
            return Beneficiary(**row._mapping)

        raise BeneficiaryNotFoundException(message=f"Beneficiary not found for id {id}")

    @classmethod
    def validate_participation(
        cls, employee_id: int, to_validate: List[Beneficiary]
    ) -> None:
        beneficiaries = cls.all(employee_id)
        beneficiaries_map = {b.id: b for b in beneficiaries}

        for item in to_validate:
            if item.participation_percent is not None and item.id is not None:
                beneficiary = beneficiaries_map.get(item.id)

                if not beneficiary:
                    item.id = None
                    beneficiaries.append(item)
                else:
                    beneficiary.participation_percent = item.participation_percent
            else:
                beneficiaries.append(item)

        participation: float = round(
            sum([b.participation_percent for b in beneficiaries]), 2
        )

        if participation > 100:
            raise BeneficiaryParticipationExceededException

    def create(self, employee_id: int) -> Beneficiary:
        validate_birth_date(self.birth_date)
        validate_phone(self.phone)

        Employee.get(employee_id)
        nationality = Nationality.get(self.nationality_id)
        self.validate_participation(employee_id, [self])

        procedure = Procedure(SP_INSERT_BENEFICIARY)
        self.employee_id = employee_id
        params = copy(self.__dict__)
        params.pop("id", None)
        params.pop("is_active", None)
        params.pop("nationality", None)

        inserted: Optional[Beneficiary] = None

        for row in procedure.execute(**params):
            inserted = Beneficiary(**row._mapping, nationality=nationality.description)

        if inserted:
            procedure.commit()
            return inserted

        raise BeneficiaryCouldNotBeCreatedException

    def update(self, to_update: Beneficiary) -> Beneficiary:
        nationality: Optional[Nationality] = None

        if to_update.birth_date is not None:
            validate_birth_date(self.birth_date)
        if to_update.phone is not None:
            validate_phone(self.phone)
        if to_update.nationality_id is not None:
            nationality = Nationality.get(to_update.nationality_id)

        for k, v in to_update.__dict__.items():
            if v is None:
                continue
            self.__setattr__(k, v)

        to_validate = [self] if self.is_active else []
        self.validate_participation(self.employee_id, to_validate)

        procedure = Procedure(SP_UPDATE_BENEFICIARY)
        params = copy(self.__dict__)
        params.pop("nationality", None)
        updated: Optional[Beneficiary] = None

        for row in procedure.execute(**params):
            updated = Beneficiary(
                **row._mapping,
                nationality=nationality.description if nationality else None,
            )

        if updated:
            procedure.commit()
            return updated

        raise BeneficiaryCouldNotBeUpdatedException

    def delete(self) -> Beneficiary:
        to_update = Beneficiary(is_active=False)
        return self.update(to_update)
