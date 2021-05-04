from fastapi import APIRouter
from app.api.v1.endpoints.rent_house import router as rent_house_route
from app.api.v1.endpoints.telegram_user import router as telegram_user_route
from app.api.v1.endpoints.attachments import router as attachment_route


router = APIRouter(prefix="/v1")

router.include_router(rent_house_route)
router.include_router(telegram_user_route)
router.include_router(attachment_route)
