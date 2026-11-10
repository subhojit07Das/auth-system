from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.routes.auth import router as auth_router

app = FastAPI(
    title="Authentication System",
    description="User authentication using FastAPI",
    version="1.0.0"
)

app.include_router(auth_router)

templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )

@app.get("/health")
def health():
    return {"status": "healthy"}
