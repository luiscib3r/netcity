from fastapi import APIRouter
from app.api.v1.endpoints.rent_house import router as rent_house_route


router = APIRouter(prefix="/v1")

router.include_router(rent_house_route)
