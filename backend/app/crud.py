from sqlalchemy.orm import Session
from app import models, security

# Usuário
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, email: str, password: str):
    hashed_password = security.get_password_hash(password)
    db_user = models.User(email=email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Categoria
def create_category(db: Session, name: str):
    category = models.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def get_categories(db: Session):
    return db.query(models.Category).all()

# Produto
def create_product(db: Session, name: str, price: float, category_id: int):
    product = models.Product(name=name, price=price, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(models.Product).all()

# Pedido
def create_order(db: Session, item: str, quantity: int):
    order = models.Order(item=item, quantity=quantity)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_orders(db: Session):
    return db.query(models.Order).all()
