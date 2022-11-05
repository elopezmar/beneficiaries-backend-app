from typing import Any
from marshmallow import Schema, post_load


class DataclassSchema(Schema):
    __model__ = None

    @post_load
    def make_dataclass(self, data, **kwargs):
        return self.__model__(**data)
