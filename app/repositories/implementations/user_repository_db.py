from sqlmodel import Session, select
from typing import Optional, List, Any
from app.models import User

class UserRepositoryDB:
    def __init__(self, session: Session, organization_id: Optional[int] = None):
        self.session = session
        self.organization_id = organization_id

    def _base_stmt(self):
        if self.organization_id is None:
            raise ValueError("organization_id must be set for UserRepositoryDB")
        return select(User).where(User.organization_id == self.organization_id) 
    
    def set_organization_id(self, organization_id: int) -> Any:
        if self.organization_id is None:
            self.organization_id = organization_id

    def get_by_id(self, user_id: int) -> Optional[User]:
        stmt = self._base_stmt().where(User.organization_id == user_id)
        return self.session.exec(stmt).first()

    def get_by_email(self, email: str) -> Optional[User]:
        stmt = self._base_stmt().where(User.email == email)
        return self.session.exec(stmt).first()

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        stmt = self._base_stmt().limit(limit).offset(skip)
        return self.session.exec(stmt).all()