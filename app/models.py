from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import Optional, List
from datetime import datetime, timezone


class Tenant(SQLModel, table=True):
    __tablename__ = "tenants"

    id:Optional[int] = Field(default=None, primary_key=True, index=True)
    name:str
    created_at:datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    users: List["User"] = Relationship(back_populates="tenant")
    workspaces: List["Workspace"] = Relationship(back_populates="tenant")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: EmailStr
    password_hash: str
    full_name: str
    tenant_id: int = Field(foreign_key="tenants.id")

    tenant: "Tenant" = Relationship(back_populates="users")
    workspaces: List["Workspace"] = Relationship(back_populates="user")


class Workspace(SQLModel, table=True):
    __tablename__ = "workspaces"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    description:str
    tenant_id: int = Field(foreign_key="tenants.id")
    create_by: int = Field(foreign_key="users.id")
    is_archived: bool = Field(default=False)

    tenant: "Tenant" = Relationship(back_populates="workspaces")
    user: "User" = Relationship(back_populates="workspaces")