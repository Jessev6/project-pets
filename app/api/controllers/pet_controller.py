from fastapi import APIRouter, HTTPException, Response

from app.domain.models.pet import Pet

router = APIRouter()

@router.get('/api/pets')
async def get_all_pets():
  # TODO: implement get_all_pets
  raise HTTPException(status_code=501)

@router.post('/api/pets', status_code=201)
async def create_pet(pet: Pet):
  # TODO: implement create_pet
  raise HTTPException(status_code=501)

@router.get('/api/pets/{id}')
async def get_pet(id: str):
  # TODO: implement get_pet
  raise HTTPException(status_code=501)

@router.put('/api/pets/{id}', status_code=202)
async def update_pet(id: str, update: Pet):
  # TODO: implement update_pet
  raise HTTPException(status_code=501)

@router.delete('/api/pets/{id}', status_code=204, response_class=Response)
async def delete_pet(id: str):
  # TODO: implement delete_pet
  raise HTTPException(status_code=501)
