from ninja import Router
from bca.api.schemas import AggregateOut, EntityIn, EntityOut, Error
from typing import List

router = Router()


@router.get("aggregates/getAllEntities", response={200: List[AggregateOut]})
async def get_aggregate_entities(request):
    # For the sake of simplicity return constant fake data.
    return 200, [
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


@router.post(
    "aggregates/{aggregate_id}/entities/{entity_id}/removeEntity",
    response={200: EntityOut, 501: Error},
)
async def remove_entity_from_aggregate(request, aggregate_id: int, entity_id: int):
    if not (aggregate_id == 0 and entity_id == 1):
        return 501, Error(
            message="For the sake of simplicity only removal of entity 1 from aggregate 0 allowed."
        )
    # For the sake of simplicity return constant fake data.
    return 200, {"uid": 1, "name": "Entity B", "data": 200}


@router.post(
    "/aggregates/{aggregate_id}/entities/{entity_id}/changeData",
    response={200: EntityOut, 501: Error},
)
async def change_entity_data(
    request, aggregate_id: int, entity_id: int, entity: EntityIn
):
    if aggregate_id != 0 and entity_id != 0:
        return 501, Error(
            message="For the sake of simplicity only mutation of aggregate 0, entity 0 allowed."
        )

    # For the sake of simplicity return fake response with mutated data.
    return 200, {"uid": 0, "name": "Entity A", "data": entity.data}
