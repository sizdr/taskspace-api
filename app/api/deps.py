from typing import Generator, Annotated 
from sqlmodel import Session
from app.core.db import engine

def get_db() -> Generator[Annotated[Session, None, None]]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, get_db()]   