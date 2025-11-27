from typing import Optional, List
from datetime import datetime
from decimal import Decimal
from enum import Enum
from sqlmodel import Field, SQLModel, Relationship

from .user import User
from .product import Product

class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    total_amount: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional[User] = Relationship(back_populates="orders")
    items: List["OrderItem"] = Relationship(back_populates="order")

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: int
    price_at_purchase: Decimal = Field(max_digits=10, decimal_places=2)

    order: Optional[Order] = Relationship(back_populates="items")
    product: Optional[Product] = Relationship(back_populates="order_items")
