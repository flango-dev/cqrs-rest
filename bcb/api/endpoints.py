from ninja import Router
from bcb.api.schemas import (
    Error,
    QueryGetAggregateEntities,
    QueryResponseGetAggregateEntities,
    CommandRemoveEntityFromAggregate,
    CommandResponseRemoveEntityFromAggregate,
    CommandChangeEntityData,
    CommandResponseChangeEntityData,
)

router = Router()


@router.post("queries", response={200: QueryResponseGetAggregateEntities, 405: Error})
async def queries(request, query: QueryGetAggregateEntities):
    match query.query.uid:
        case "get_aggregate_entities":
            return 200, QueryResponseGetAggregateEntities(
                aggregates=[
                    {
                        "uid": 0,
                        "name": "Aggregate A",
                        "entities": [
                            {"uid": 0, "name": "Entity A", "data": 100},
                            {"uid": 1, "name": "Entity B", "data": 200},
                        ],
                    },
                    {
                        "uid": 1,
                        "name": "Aggregate B",
                        "entities": [
                            {"uid": 0, "name": "Entity C", "data": 300},
                            {"uid": 1, "name": "Entity D", "data": 400},
                        ],
                    },
                ]
            )
        case _:
            return 405, Error(
                message="Query method not allowed. Supported query methods: get_aggregate_entities"
            )


@router.post(
    "commands",
    response={
        200: CommandResponseRemoveEntityFromAggregate | CommandResponseChangeEntityData,
        405: Error,
        501: Error,
    },
)
async def remove_entity_from_aggregate(
    request, command: CommandRemoveEntityFromAggregate | CommandChangeEntityData
):
    match command.command.uid:
        case "remove_entity_from_aggregate":
            if not (command.aggregate_id == 0 and command.entity_id == 1):
                return 501, Error(
                    message="For the sake of simplicity only removal of entity 1 from aggregate 0 allowed."
                )
            # For the sake of simplicity return constant fake data.
            return 200, CommandResponseRemoveEntityFromAggregate(
                entity={"uid": 1, "name": "Entity B", "data": 200}
            )
        case "change_entity_data":
            if command.aggregate_id != 0 and command.entity_id != 0:
                return 501, Error(
                    message="For the sake of simplicity only mutation of aggregate 0, entity 0 allowed."
                )
            # For the sake of simplicity return fake response with mutated data.
            return 200, CommandResponseChangeEntityData(
                entity={"uid": 0, "name": "Entity A", "data": command.entity.data}
            )
        case _:
            return 405, Error(
                message="Command method not allowed. Supported command methods: remove_entity_from_aggregate, change_entity_data."
            )
