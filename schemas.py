from pydantic import BaseModel
from datetime import date, datetime

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