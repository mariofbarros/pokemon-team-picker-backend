from sqlalchemy import Column, DateTime, Integer, JSON, String, func

from .database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    pokemons = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
