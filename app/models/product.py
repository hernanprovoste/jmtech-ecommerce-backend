from typing import Optional, Any, List, TYPE_CHECKING
from datetime import datetime
from decimal import Decimal
from enum import Enum
from sqlmodel import Field, SQLModel, Column, Relationship
from sqlalchemy import JSON

if TYPE_CHECKING:
    from .order import OrderItem

class Category(str, Enum):
    CPU = "CPU"
    GPU = "GPU"
    MOTHERBOARD = "MOTHERBOARD"
    RAM = "RAM"
    DRONE = "DRONE"
    DOMOTICS = "DOMOTICS"
    PERIPHERAL = "PERIPHERAL"
    PSU = "PSU"
    CASE = "CASE"
    STORAGE = "STORAGE"

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    slug: str = Field(unique=True, index=True)
    description: Optional[str] = None
    price: Decimal = Field(default=0, max_digits=10, decimal_places=2)
    stock: int = Field(default=0)
    image_url: Optional[str] = None
    category: Category
    specs: Optional[Any] = Field(default=None, sa_column=Column(JSON))
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

    order_items: List["OrderItem"] = Relationship(back_populates="product")
