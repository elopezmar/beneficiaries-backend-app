from typing import Optional
from models.admin import Admin


def authenticate(username, password) -> Optional[Admin]:
    admin = Admin.get_by_username(username)
    if admin and admin.password == password:
        return admin


def identity(payload) -> Optional[Admin]:
    return Admin.get(payload["identity"])
