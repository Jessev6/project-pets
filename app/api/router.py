from fastapi import APIRouter

from app.api.controllers.health_controller import router as health
from app.api.controllers.hello_controller import router as hello
from app.api.controllers.pet_controller import router as pets
 
router = APIRouter()
router.include_router(health)
router.include_router(hello)
router.include_router(pets)
