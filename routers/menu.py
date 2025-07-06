from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/menu", tags=["Menü"])

@router.post("/", response_model=schemas.MenuItemOut)
def create_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    menu_item = models.MenuItem(**item.dict())
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item

@router.get("/", response_model=list[schemas.MenuItemOut])
def get_menu(language: str = "uz", db: Session = Depends(get_db)):
    return db.query(models.MenuItem).filter(models.MenuItem.language == language).order_by(models.MenuItem.order).all()
