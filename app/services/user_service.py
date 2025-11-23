from app.repositories.interfaces.user_repository import UserRepository
from app.schemas import UserCreate
from app.models import User
from app.core.security import get_password_hash
from fastapi import HTTPException
from typing import Optional
from app.models import RoleEnum

class UserService:
    def __init__(self,user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_create: UserCreate, organization_id: int, role: Optional[RoleEnum] = None) -> User:
        self.user_repo.set_organization_id(organization_id)
        if self.user_repo.get_by_email(user_create.email):
            raise HTTPException(status_code=400, detail="Email already registered")
        user_dict = user_create.model_dump(exclude={"password"})
        user_dict['password_hash'] = get_password_hash(user_create.password)
        user_dict['organization_id'] = organization_id
        if role is not None:
            user_dict['role'] = role
        user_model = User(**user_dict)
        user = self.user_repo.create(user_model)
        return user
    

    