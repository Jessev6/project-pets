from fastapi import APIRouter

from app.api.controllers.hello_controller import router as hello
 
router = APIRouter()
router.include_router(hello)
