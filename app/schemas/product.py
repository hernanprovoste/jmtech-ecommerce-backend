from typing import Optional, Any, Dict
from decimal import Decimal
from pydantic import BaseModel, model_validator
from app.models.product import Category

class ProductBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    price: Decimal
    stock: int
    image_url: Optional[str] = None
    category: Category
    specs: Optional[Dict[str, Any]] = None

class ProductCreate(ProductBase):
    @model_validator(mode='after')
    def validate_specs(self) -> 'ProductCreate':
        category = self.category
        specs = self.specs or {}

        required_keys = {
            Category.CPU: {"socket", "cores", "base_clock"},
            Category.MOTHERBOARD: {"socket", "form_factor", "ram_type"},
            Category.RAM: {"type", "capacity", "speed"},
        }

        if category in required_keys:
            missing = required_keys[category] - specs.keys()
            if missing:
                raise ValueError(f"For category {category.value}, specs must contain: {', '.join(missing)}")
        
        return self

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
    image_url: Optional[str] = None
    category: Optional[Category] = None
    specs: Optional[Dict[str, Any]] = None

class ProductRead(ProductBase):
    id: int
