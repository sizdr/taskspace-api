from typing import Protocol, Optional, List
from app.models import User

class UserRepository(Protocol):
    def get_by_id(self, tenant_id:int, user_id: int) -> Optional[User]:
        ...

    def get_by_email(self, tenant_id:int, email: str) -> Optional[User]:
        ...

    def create(self, user: User) -> User:
        ...

    def list(self, tenant_id:int, skip: int = 0, limit: int = 100) -> List[User]:
        ...