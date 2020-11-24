from fastapi import APIRouter, HTTPException, Response

from app.domain.models.pet import Pet

router = APIRouter()

@router.get('/api/pets')
async def get_all_pets():
  return await PetRepository.get_all()

@router.post('/api/pets', status_code=201)
async def create_pet(pet: Pet):
  return await PetRepository.create(pet)

@router.get('/api/pets/{id}')
async def get_pet(id: str):
  pet = await PetRepository.get_by_id(id)
  if pet is None:
    raise HTTPException(status_code=404, detail="Pet not found")

  return pet

@router.put('/api/pets/{id}', status_code=202)
async def update_pet(id: str, update: Pet):
  pet = await PetRepository.update(id, update)
  if pet is None:
    raise HTTPException(status_code=404, detail="Pet not found")

  return pet

@router.delete('/api/pets/{id}', status_code=204, response_class=Response)
async def delete_pet(id: str):
  if not await PetRepository.delete(id):
    raise HTTPException(status_code=404, detail="Pet not found")

  return
