from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .tenant import Tenant
    from .user import User

class Workspace(SQLModel, table=True):
    __tablename__ = "workspaces"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    description:str
    tenant_id: int = Field(foreign_key="tenants.id")
    create_by: int = Field(foreign_key="users.id")
    is_archived: bool

    tenant: "Tenant" = Relationship(back_populates="workspaces")
    user: "User" = Relationship(back_populates="workspaces")
