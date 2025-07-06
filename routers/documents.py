from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/documents", tags=["Me’yoriy hujjatlar"])

@router.post("/", response_model=schemas.DocumentOut)
def create_document(doc: schemas.DocumentCreate, db: Session = Depends(get_db)):
    new_doc = models.Document(**doc.dict())
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

@router.get("/{category}", response_model=list[schemas.DocumentOut])
def list_documents_by_category(category: str, db: Session = Depends(get_db)):
    docs = db.query(models.Document).filter(models.Document.category == category).order_by(models.Document.published_date.desc()).all()
    if not docs:
        raise HTTPException(status_code=404, detail="Hujjatlar topilmadi")
    return docs