from sqlmodel import Session, select
from typing import Optional, List
from app.models import User

class UserRepositoryDB:
    def __init__(self, session: Session, tenant_id:int):
        self.session = session
        self.tenant_id = tenant_id

    def _base_stmt(self):
        return select(User).where(User.tenant_id == self.tenant_id) 

    def get_by_id(self, user_id: int) -> Optional[User]:
        stmt = self._base_stmt().where(User.tenant_id == user_id)
        return self.session.exec(stmt).first()

    def get_by_email(self, email: str) -> Optional[User]:
        stmt = self._base_stmt().where(User.email == email)
        return self.session.exec(stmt).first()

    def create(self, user: User) -> User:
        user.tenant_id = self.tenant_id
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def list(self, skip: int = 0, limit: int = 100) -> List[User]:
        stmt = self._base_stmt().limit(limit).offset(skip)
        return self.session.exec(stmt).all()