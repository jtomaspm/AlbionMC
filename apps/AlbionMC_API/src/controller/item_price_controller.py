from dataclasses import asdict
from datetime import datetime
from typing import Dict, List
from fastapi import APIRouter, Depends, HTTPException, Request
from src.core.entities.item import Item
from src.controller.models.price_from_target_request import ItemPriceFromTarget
from src.core.entities.item_price import ItemPrice
from src.repository.item_price_repository import ItemPriceRepository

item_price_router = APIRouter(prefix="/item_prices", tags=["Item Prices"])

from src.dependencies import configure_injector
injector = configure_injector()

def all_letters_capitalized(string):
    for char in string:
        if char.isalpha() and not char.isupper():
            return False
    return True

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
def create_item_price(request: Request, item_price: ItemPrice, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    item_price_repo.new(item_price, request.state.user['login'])
    return {"message": "Item price created successfully"}

@item_price_router.post("/batch")
def create_item_prices(request: Request, item_prices: List[ItemPrice], item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    try:
        item_price_repo.new_batch(item_prices, request.state.user['login'])
        return {"message": "Item prices created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@item_price_router.put("/{item_id}")
def update_item_price(request: Request, item_id: int, created_at: str, item_price: ItemPrice, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    existing_item_price = item_price_repo.get(item_id, datetime.fromtimestamp(created_at))
    if existing_item_price:
        item_price_repo.update(item_price, request.state.user['login'])
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

@item_price_router.post("/target")
def create_item_price_from_target(request: Request, record: ItemPriceFromTarget, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    if(record.target.isnumeric()):
        item = Item(**{
            'id': int(record.target),
            'unique_name': '',
            'name': '',
            'tags': [],
            'data_source_id': 0
        })
        item_price_repo.new_from_item(item=item, record=record.item_price, user_name=request.state.user['login'])
    elif all_letters_capitalized(record.target):
        item = Item(**{
            'unique_name': record.target,
            'name': '',
            'tags': [],
            'data_source_id': 0
        })
        item_price_repo.new_from_item(item=item, record=record.item_price, user_name=request.state.user['login'])
    else:
        item = Item(**{
            'unique_name': '',
            'name': record.target,
            'tags': [],
            'data_source_id': 0
        })
        item_price_repo.new_from_item(item=item, record=record.item_price, user_name=request.state.user['login'])
    return {"message": "Item price created successfully"}

@item_price_router.post("/target/batch")
def create_item_prices_from_target(request: Request, records: List[ItemPriceFromTarget], item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))):
    data: Dict[Item,ItemPrice] = {}
    for record in records:
        if(record.target.isnumeric()):
            item = Item(**{
                'id': int(record.target),
                'unique_name': '',
                'name': '',
                'tags': [],
                'data_source_id': 0
            })
            data[item] = record.item_price
        elif all_letters_capitalized(record.target):
            item = Item(**{
                'unique_name': record.target,
                'name': '',
                'tags': [],
                'data_source_id': 0
            })
            data[item] = record.item_price
        else:
            item = Item(**{
                'unique_name': '',
                'name': record.target,
                'tags': [],
                'data_source_id': 0
            })
            data[item] = record.item_price
    item_price_repo.new_batch_from_items(data=data, user_name=request.state.user['login'])
    return {"message": "Item price created successfully"}