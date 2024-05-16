from datetime import datetime
from typing import List
from fastapi import APIRouter, Depends, Request
from src.core.entities.data_source import DataSource
from src.core.entities.item_details import ItemDetails
from src.repository.data_source_repository import DataSourceRepository
from src.repository.item_repository import ItemRepository
from src.core.entities.item import Item
from src.core.entities.item_price import ItemPrice
from src.repository.item_price_repository import ItemPriceRepository

item_detail_router = APIRouter(prefix="/item_details", tags=["Item Details"])

from src.dependencies import configure_injector
injector = configure_injector()

@item_detail_router.get("/")
def get_item_details(item_id: int, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))) -> List[ItemPrice]:
    pass

@item_detail_router.get("/{item_id}")
def get_item_detail(item_id: int, item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository))) -> ItemPrice:
    pass

@item_detail_router.post("/")
def create_item_price(request: Request, 
                      record: ItemDetails, 
                      item_price_repo: ItemPriceRepository = Depends(lambda: injector.get(ItemPriceRepository)),
                      data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository)),
                      item_repo: ItemRepository = Depends(lambda: injector.get(ItemRepository)),
                      ):
    ds = data_source_repo.get_by_name(record.data_source)
    user_name = request.state.user['login']
    if (ds == None):
        ds = DataSource(**{
            'name': record.data_source,
            'trust_level': 0
        })
        data_source_repo.new(record=ds, user_name=user_name)
    if (len(record.prices) > 0):
        for price in record.prices:
            ip = ItemPrice()
            ip.city = price.city
            ip.item_id = record.id
            ip.price = price.price
            item_price_repo.new(record=ip, user_name=user_name)
    ds = data_source_repo.get_by_name(record.data_source)
    i = Item(**{
                "unique_name" : record.unique_name,
                "name" : record.name,
                "tags" : record.tags,
                "tier" : record.tier,
                "enchant" : record.enchant,
                "description" : record.description,
                "data_source_id" : ds.id,
            })
    item_repo.new(record=i, user_name=user_name)
    return {"message": "Item created successfully"}

