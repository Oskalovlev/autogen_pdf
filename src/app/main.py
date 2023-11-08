from fastapi import FastAPI

from src.app.core.config import settings

app = FastAPI(title=settings.base.APP_TITLE)


# @app.get('/')
# def


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}
