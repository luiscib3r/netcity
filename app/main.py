from fastapi import FastAPI, Depends
from fastapi.security.api_key import APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import HTTPException

from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.responses import RedirectResponse, JSONResponse

from app.auth.api_key import get_api_key, API_KEY_NAME
from app.api import router as api_router

app = FastAPI(title="NetCity", docs_url=None, redoc_url=None, openapi_url=None)
app.include_router(api_router)


@app.get("/", tags=["NetCity"])
async def homepage():
    return "NetCity is UP"


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test",
                    version=1, routes=app.routes)
    )
    return response


@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        httponly=True,
        max_age=1800,
        expires=1800,
    )

    return response


@app.get("/logout", tags=["NetCity"])
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie(API_KEY_NAME)
    return response
