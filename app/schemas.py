from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


# Pydantic request/response models. Shapes what the API accepts and returns;
# Team persistence itself is handled by models.Team + crud.py.


class Pokemon(BaseModel):
    """A single team slot, as fetched from PokeAPI by the frontend."""

    id: int
    name: str
    sprite: Optional[str] = None
    # Defaults to empty so teams saved before types were stored still load.
    types: List[str] = Field(default_factory=list)


class TeamBase(BaseModel):
    name: str
    # Teams are always exactly 6 Pokemon, enforced here.
    pokemons: List[Pokemon] = Field(min_length=6, max_length=6)


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class TeamOut(TeamBase):
    """What's returned to clients: adds the DB-assigned id/timestamp."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
