from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db
from app.schemas.category import CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categorias"])

@router.post("/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category.name)

@router.get("/")
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)
