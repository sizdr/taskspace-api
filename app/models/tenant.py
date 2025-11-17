from sqlmodel import SQLModel, Field, DateTime, Relationship
from typing import Optional, TYPE_CHECKING, List
from datetime import datetime, timezone

if TYPE_CHECKING:
    from .user import User
    from .workspace import Workspace

class Tenant(SQLModel, table=True):
    __tablename__ = "tenants"

    id:Optional[int] = Field(default=None, primary_key=True, index=True)
    name:str
    created_at:datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    users: List["User"] = Relationship(back_populates="tenant")
    workspaces: List["Workspace"] = Relationship(back_populates="tenant")
