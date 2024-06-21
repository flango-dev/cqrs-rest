from typing import List
from ninja import Schema


class EntityIn(Schema):
    data: int


class EntityOut(Schema):
    uid: int
    name: str
    data: int


class AggregateOut(Schema):
    uid: int
    name: str
    entities: List[EntityOut]


class Error(Schema):
    message: str
