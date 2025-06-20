from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db
from app.schemas.order import OrderCreate

router = APIRouter(prefix="/orders", tags=["Pedidos"])

@router.post("/")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order.item, order.quantity)

@router.get("/")
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)
