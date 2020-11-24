from time import time

from fastapi import FastAPI

from app.api.router import router

def init_app() -> FastAPI:
  application = FastAPI(title="Hello World API", version="0.0.1")
  application.include_router(router)

  return application

app = init_app()