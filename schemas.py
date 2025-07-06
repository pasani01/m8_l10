from pydantic import BaseModel
from datetime import date, datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class MenuItemCreate(BaseModel):
    title: str
    order: int
    language: str = "uz"

class MenuItemOut(MenuItemCreate):
    id: int

    class Config:
        from_attributes = True 

class DocumentCreate(BaseModel):
    title: str
    category: str
    file_url: str
    published_date: date
    language: str = "uz"

class DocumentOut(DocumentCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
