# FastAPI app: REST CRUD for saved Pokemon teams. Pokemon data itself comes
# from PokeAPI, fetched client-side; this API only stores the finished teams.
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import engine, get_db

# Creates the teams table on startup if it doesn't exist yet (no migrations).
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pokemon Team Picker API")

# Wide open CORS since this is a small public demo API with no auth.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/teams", response_model=list[schemas.TeamOut])
def list_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)


@app.post("/teams", response_model=schemas.TeamOut, status_code=201)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)


@app.get("/teams/{team_id}", response_model=schemas.TeamOut)
def get_team(team_id: int, db: Session = Depends(get_db)):
    db_team = crud.get_team(db, team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@app.put("/teams/{team_id}", response_model=schemas.TeamOut)
def update_team(team_id: int, team: schemas.TeamUpdate, db: Session = Depends(get_db)):
    db_team = crud.update_team(db, team_id, team)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return db_team


@app.delete("/teams/{team_id}", status_code=204)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    db_team = crud.delete_team(db, team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
