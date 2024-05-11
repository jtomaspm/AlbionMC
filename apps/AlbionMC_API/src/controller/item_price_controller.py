from dataclasses import asdict
from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.core.entities.item_price import ItemPrice
from src.repository.item_price_repository import ItemPriceRepository

item_price_router = APIRouter(prefix="/item_prices", tags=["Item Prices"])

from src.dependencies import configure_injector
injector = configure_injector()

@item_price_router.get("/")
def get_item_prices(item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))) -> List[ItemPrice]:
    return item_price_repo.get_all()

@item_price_router.get("/{item_id}")
def get_item_price(item_id: int, created_at: str, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))) -> ItemPrice:
    item_price = item_price_repo.get(item_id, datetime.fromtimestamp(created_at))
    if item_price:
        return item_price
    else:
        raise HTTPException(status_code=404, detail="Item price not found")

@item_price_router.post("/")
def create_item_price(item_price: ItemPrice, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    item_price_repo.new(item_price)
    return {"message": "Item price created successfully"}

@item_price_router.post("/batch")
def create_item_prices(item_prices: List[ItemPrice], item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    try:
        item_price_repo.new_batch(item_prices)
        return {"message": "Item prices created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@item_price_router.put("/{item_id}")
def update_item_price(item_id: int, created_at: str, item_price: ItemPrice, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    existing_item_price = item_price_repo.get(item_id, datetime.fromtimestamp(created_at))
    if existing_item_price:
        item_price_repo.update(item_price)
        return {"message": "Item price updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item price not found")

@item_price_router.delete("/{item_id}")
def delete_item_price(item_id: int, created_at: str, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    existing_item_price = item_price_repo.get(item_id, datetime.fromtimestamp(created_at))
    if existing_item_price:
        item_price_repo.delete(item_id, datetime.fromtimestamp(created_at))
        return {"message": "Item price deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item price not found")