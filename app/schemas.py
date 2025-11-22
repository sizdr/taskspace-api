from pydantic import BaseModel, EmailStr

class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    pass

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class UserCreate(UserBase):
    password: str

class OrganizationCreateForm(BaseModel):
    user: UserCreate
    organization: OrganizationCreate