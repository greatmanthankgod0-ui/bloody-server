from pydantic import BaseModel

class Order(BaseModel):
    user_id: int
    product_id: int
    quantity: int
