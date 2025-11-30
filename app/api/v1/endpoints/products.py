from typing import List, Optional
from decimal import Decimal
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from app.api.deps import SessionDep
from app.models.product import Product, Category
from app.schemas.product import ProductCreate, ProductRead, ProductUpdate

router = APIRouter()

@router.post("/", response_model=ProductRead)
def create_product(*, session: SessionDep, product: ProductCreate):
    db_product = Product.model_validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/", response_model=List[ProductRead])
def read_products(
    *,
    session: SessionDep,
    offset: int = 0,
    limit: int = 100,
    category: Optional[Category] = None,
    min_price: Optional[Decimal] = None,
    max_price: Optional[Decimal] = None,
):
    query = select(Product)
    if category:
        query = query.where(Product.category == category.upper())
    if min_price is not None:
        query = query.where(Product.price >= min_price)
    if max_price is not None:
        query = query.where(Product.price <= max_price)
    
    query = query.offset(offset).limit(limit)
    products = session.exec(query).all()
    return products

@router.get("/{product_id}", response_model=ProductRead)
def read_product(*, session: SessionDep, product_id: int):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
def update_product(*, session: SessionDep, product_id: int, product_in: ProductUpdate):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product_data = product_in.model_dump(exclude_unset=True)
    db_product.sqlmodel_update(product_data)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.delete("/{product_id}")
def delete_product(*, session: SessionDep, product_id: int):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product)
    session.commit()
    return {"ok": True}
