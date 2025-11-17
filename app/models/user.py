from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .tenant import Tenant

class User(SQLModel, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: EmailStr
    password_hash: str
    full_name: str
    tenant_id: int = Field(foreign_key="tenants.id")

    tenant: "Tenant" = Relationship(back_populates="users")