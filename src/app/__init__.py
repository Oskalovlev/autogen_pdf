from fastapi import FastAPI

from src.app.core.config import settings
from src.app.core.server import Server


def create_app(_=None) -> FastAPI:
    app = FastAPI(title=settings.base.APP_TITLE)

    return Server(app).get_app()
