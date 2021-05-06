from config import odoo

from fastapi import APIRouter, Depends, Query, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.security.api_key import APIKey
from app.auth.api_key import get_api_key
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from core.models import Attachment
from core.crud.attachment import crud_create_attachment, crud_get_attachment
from core.errors.odoo_exception import OdooException

from typing import List
import base64


router = APIRouter(prefix="/attachments", tags=["Attachments"])


@router.get("/", response_model=List[Attachment])
async def get_attachments(
    api_key: APIKey = Depends(get_api_key),
    limit: int = Query(20),
    offset: int = Query(0),
    domain: List = Query([]),
):
    domain = [filter.strip("[]").replace(" ", "").split(",")
              for filter in domain]
    try:
        return crud_get_attachment(odoo, domain, limit=limit, offset=offset)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/")
async def create_attachment(
    attachment: Attachment,
    api_key: APIKey = Depends(get_api_key),
):
    try:
        return crud_create_attachment(odoo, attachment)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.post("/upload")
async def upload_attachment(
    file: UploadFile = File(...),
    api_key: APIKey = Depends(get_api_key),
):
    try:
        data = await file.read()

        file_content = base64.b64encode(data)

        return crud_create_attachment(odoo, Attachment(
            name=file.filename,
            datas=file_content
        ))
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )


@router.get("/download")
async def download_attachment(
    attachment_id: int,
):
    try:
        files = crud_get_attachment(odoo, [["id", "=", attachment_id]])

        if len(files) == 0 or not files[0].datas:
            raise HTTPException(status_code=404, detail="Item not found")

        file_content = base64.b64decode(files[0].datas)

        with open(f"/tmp/{files[0].name}", "wb+") as f:
            print(f"/tmp/{files[0].name}")
            f.write(file_content)

        return FileResponse(f"/tmp/{files[0].name}", filename=files[0].name)
    except OdooException as e:
        raise HTTPException(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.message,
        )
