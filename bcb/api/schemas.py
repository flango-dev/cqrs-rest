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


class Query(Schema):
    uid: str


class QueryGetAggregateEntities(Schema):
    query: Query


class QueryResponseGetAggregateEntities(Schema):
    aggregates: List[AggregateOut]


class Command(Schema):
    uid: str


class CommandRemoveEntityFromAggregate(Schema):
    command: Command
    aggregate_id: int
    entity_id: int


class CommandChangeEntityData(Schema):
    command: Command
    aggregate_id: int
    entity_id: int
    entity: EntityIn


class CommandResponseRemoveEntityFromAggregate(Schema):
    entity: EntityOut


class CommandResponseChangeEntityData(Schema):
    entity: EntityOut
