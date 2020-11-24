from fastapi import APIRouter

from app.api.controllers.hello_controller import router as hello
from app.api.controllers.pet_controller import router as pets
 
router = APIRouter()
router.include_router(hello)
router.include_router(pets)
