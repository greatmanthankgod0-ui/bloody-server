from fastapi import APIRouter
from app.schemas.order import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

orders = []


@router.get("/")
async def get_orders():
    return orders


@router.post("/")
async def create_order(order: Order):
    orders.append(order)
    return {
        "message": "Order created",
        "order": order
    }


@router.get("/{order_id}")
async def get_order(order_id: int):
    return {
        "order_id": order_id
    }
