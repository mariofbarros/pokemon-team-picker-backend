# SQLAlchemy engine/session setup, shared by models.py and crud.py.
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Defaults to a local SQLite file; override via env var (e.g. Postgres) in production.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./teams.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# FastAPI dependency: yields a session per-request and always closes it.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
