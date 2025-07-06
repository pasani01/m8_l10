from sqlalchemy import Column, Integer, String, Date, DateTime
from datetime import datetime
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)  # e.g. qonunlar, standartlar, texnik, ...
    file_url = Column(String)
    published_date = Column(Date)
    language = Column(String, default="uz")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)