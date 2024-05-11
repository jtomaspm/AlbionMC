from dataclasses import asdict
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.core.entities.item import Item
from src.repository.item_repository import ItemRepository


item_router = APIRouter(prefix="/items", tags=["Items"])

from src.dependencies import configure_injector
injector = configure_injector()


@item_router.get("/")
def get(item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))) -> List[Item]:
    return item_repo.get_all()

@item_router.get("/{item_id}")
def get_item(item_id: int, item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))) -> Item:
    item = item_repo.get(item_id)
    if item:
        return item
    else:
        raise HTTPException(status_code=404)

@item_router.post("/")
def create_item(item: Item, item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))):
    item_repo.new(item)
    return {"message": "Item created successfully"}

@item_router.post("/batch")
def create_items(items: List[Item], item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))):
    try:
        item_repo.new_batch(items)
        return {"message": "Items created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@item_router.put("/{item_id}")
def update_item(item_id: int, item: Item, item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))):
    existing_item = item_repo.get(item_id)
    if existing_item:
        item.id = item_id
        item_repo.update(item)
        return {"message": "Item updated successfully"}
    else:
        raise HTTPException(status_code=404)

@item_router.delete("/{item_id}")
def delete_item(item_id: int, item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository))):
    existing_item = item_repo.get(item_id)
    if existing_item:
        item_repo.delete(item_id)
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404)