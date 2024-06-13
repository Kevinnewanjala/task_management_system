
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = "sqlite:///./database/task_management_system.db"

def create_db_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()