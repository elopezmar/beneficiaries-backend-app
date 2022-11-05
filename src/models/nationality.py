from __future__ import annotations
from typing import List
from dataclasses import dataclass

from services.database.procedure import Procedure
from services.database.constants import SP_ALL_NATIONALITIES, SP_GET_NATIONALITY
from services.exceptions.nationality import NationalityNotFoundException


@dataclass
class Nationality:
    id: int
    description: int

    @classmethod
    def all(cls) -> List[Nationality]:
        procedure = Procedure(SP_ALL_NATIONALITIES)
        results: List[Nationality] = []

        for row in procedure.execute():
            results.append(Nationality(**row._mapping))

        return results

    @classmethod
    def get(cls, id: int) -> Nationality:
        procedure = Procedure(SP_GET_NATIONALITY)

        for row in procedure.execute(id=id):
            return Nationality(**row._mapping)

        raise NationalityNotFoundException(message=f"Nationality not found for id {id}")
