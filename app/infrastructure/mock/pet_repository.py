from app.models.pet import Pet

from uuid import uuid4

pets = []

class PetRepository:

  @staticmethod
  async def get_all():
    return pets
  
  @staticmethod
  async def get_by_id(id):
    return next((pet for pet in pets if pet.id == id), None)

  @staticmethod
  async def create(pet: Pet):
    pet.id = str(uuid4())
    pets.append(pet)
    return pet

  @staticmethod
  async def update(id, new: Pet):
    pet = await PetRepository.get_by_id(id)
    if pet is None:
      return None

    return pet.update(new)

  @staticmethod
  async def delete(id):
    for pet in pets:
      if pet.id == id:
        pets.remove(pet)
        return True
    
    return False