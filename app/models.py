from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import Optional, List
from datetime import datetime, timezone


class Organization(SQLModel, table=True):
    __tablename__ = "organizations"

    id:Optional[int] = Field(default=None, primary_key=True, index=True)
    name:str
    created_at:datetime = Field(default_factory= lambda: datetime.now(timezone.utc))

    users: List["User"] = Relationship(back_populates="organization")
    workspaces: List["Workspace"] = Relationship(back_populates="organization")


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: EmailStr
    password_hash: str
    full_name: str
    organization_id: int = Field(foreign_key="organizations.id")

    organization: "Organization" = Relationship(back_populates="users")
    workspaces: List["Workspace"] = Relationship(back_populates="user")


class Workspace(SQLModel, table=True):
    __tablename__ = "workspaces"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str
    description:str
    organization_id: int = Field(foreign_key="organizations.id")
    created_by: int = Field(foreign_key="users.id")
    is_archived: bool = Field(default=False)

    organization: "Organization" = Relationship(back_populates="workspaces")
    creator: "User" = Relationship(back_populates="workspaces")