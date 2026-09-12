from sqlalchemy.orm import Session

from . import models, schemas


def get_teams(db: Session):
    return db.query(models.Team).order_by(models.Team.id).all()


def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()


def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(
        name=team.name,
        pokemons=[p.model_dump() for p in team.pokemons],
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def update_team(db: Session, team_id: int, team: schemas.TeamUpdate):
    db_team = get_team(db, team_id)
    if db_team is None:
        return None
    db_team.name = team.name
    db_team.pokemons = [p.model_dump() for p in team.pokemons]
    db.commit()
    db.refresh(db_team)
    return db_team


def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if db_team is None:
        return None
    db.delete(db_team)
    db.commit()
    return db_team
