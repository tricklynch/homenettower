from functools import cache
from fastapi import FastAPI
from homenettower.routes import router


@cache
def create_app():
    app = FastAPI()
    app.include_router(router)
    return app
