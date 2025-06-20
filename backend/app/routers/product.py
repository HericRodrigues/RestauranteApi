from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db
from app.schemas.product import ProductCreate

router = APIRouter(prefix="/products", tags=["Produtos"])

@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product.name, product.price, product.category_id)

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    return crud.get_products(db)
