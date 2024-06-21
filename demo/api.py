from ninja import NinjaAPI
from bca.api.endpoints import router as bca_router

TITLE: str = "Demo showcasing common, CQRS-compatible RESTful API design variants"

api = NinjaAPI(title=TITLE)

api.add_router("/bca/", bca_router)
