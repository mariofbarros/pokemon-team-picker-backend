from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class Pokemon(BaseModel):
    id: int
    name: str
    sprite: Optional[str] = None
    # Defaults to empty so teams saved before types were stored still load.
    types: List[str] = Field(default_factory=list)


class TeamBase(BaseModel):
    name: str
    pokemons: List[Pokemon] = Field(min_length=6, max_length=6)


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass


class TeamOut(TeamBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
