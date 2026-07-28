from fastapi import APIRouter
from app.schemas.product import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

products = []


@router.get("/")
async def get_products():
    return products


@router.post("/")
async def create_product(product: Product):
    products.append(product)
    return {
        "message": "Product created",
        "product": product
    }


@router.get("/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id
    }
