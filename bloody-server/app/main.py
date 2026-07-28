from app.api import auth
from app.api import orders
from app.api import products
from app.api import users
from app.api import auth
from fastapi import FastAPI

from app.api import health, auth, users, products, orders
from app.database.session import Base, engine
from app.core.exceptions import register_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bloody Server",
    description="Shared Development Server",
    version="0.1.0"
)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(auth.router)

register_exception_handlers(app)
