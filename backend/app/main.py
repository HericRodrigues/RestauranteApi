from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import auth, category, product, order

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(order.router)

@app.get("/")
def root():
    return {"message": "API do Restaurante rodando 🚀"}
