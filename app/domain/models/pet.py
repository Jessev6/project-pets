from typing import Optional

from pydantic import BaseModel

class Pet(BaseModel):
  id: Optional[str] = None
  name: str
  animal: str
  birthday: Optional[str] = None
  color: Optional[str] = None

  def update(self, pet):
    self.name = pet.name if pet.name is not None else self.name
    self.animal = pet.animal if pet.animal is not None else self.animal
    self.birthday = pet.birthday if pet.birthday is not None else self.birthday
    self.color = pet.color if pet.color is not None else self.color

    return self
