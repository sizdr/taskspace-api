from sqlmodel import SQLModel, Field, DateTime
from typing import Optional

class Tenant(SQLModel):
    id:Optional[int] = Field(default=None, primary_key=True, index=True)
    name:str
    created_at:DateTime