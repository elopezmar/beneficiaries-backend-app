from __future__ import annotations
from typing import Optional
from dataclasses import dataclass

from services.database.procedure import Procedure
from services.database.constants import SP_GET_ADMIN, SP_GET_ADMIN_BY_USERNAME


@dataclass
class Admin:
    id: int
    username: int
    password: str

    @classmethod
    def get(cls, id: int) -> Optional[Admin]:
        procedure = Procedure(SP_GET_ADMIN)

        for row in procedure.execute(id=id):
            return Admin(**row._mapping)

    @classmethod
    def get_by_username(cls, username: str) -> Optional[Admin]:
        procedure = Procedure(SP_GET_ADMIN_BY_USERNAME)

        for row in procedure.execute(username=username):
            return Admin(**row._mapping)
