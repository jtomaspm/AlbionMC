from src.repository.crafting_slot_repository import CraftingSlotRepository
from dataclasses import asdict
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.core.entities.crafting_slot import CraftingSlot
from fastapi import APIRouter, Depends, HTTPException
from dataclasses import asdict
from typing import List

crafting_slot_router = APIRouter(prefix="/crafting_slots")

from src.dependencies import configure_injector
injector = configure_injector()

@crafting_slot_router.get("/")
def get_crafting_slots(crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    return [asdict(cs) for cs in crafting_slot_repo.get_all()]

@crafting_slot_router.get("/{craft_id}/{destination_item_id}/{source_item_id}")
def get_crafting_slot(craft_id: int, destination_item_id: int, source_item_id: int, crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    crafting_slot = crafting_slot_repo.get(craft_id, destination_item_id, source_item_id)
    if crafting_slot:
        return asdict(crafting_slot)
    else:
        raise HTTPException(status_code=404, detail="Crafting slot not found")

@crafting_slot_router.post("/")
def create_crafting_slot(crafting_slot: CraftingSlot, crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    crafting_slot_repo.new(crafting_slot)
    return {"message": "Crafting slot created successfully"}

@crafting_slot_router.post("/batch")
def create_crafting_slots(crafting_slots: List[CraftingSlot], crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    try:
        crafting_slot_repo.new_batch(crafting_slots)
        return {"message": "Crafting slots created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@crafting_slot_router.put("/{craft_id}/{destination_item_id}/{source_item_id}")
def update_crafting_slot(craft_id: int, destination_item_id: int, source_item_id: int, crafting_slot: CraftingSlot, crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    existing_crafting_slot = crafting_slot_repo.get(craft_id, destination_item_id, source_item_id)
    if existing_crafting_slot:
        crafting_slot_repo.update(crafting_slot)
        return {"message": "Crafting slot updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Crafting slot not found")

@crafting_slot_router.delete("/{craft_id}/{destination_item_id}/{source_item_id}")
def delete_crafting_slot(craft_id: int, destination_item_id: int, source_item_id: int, crafting_slot_repo: CraftingSlotRepository = Depends(lambda: injector.get(CraftingSlotRepository))):
    existing_crafting_slot = crafting_slot_repo.get(craft_id, destination_item_id, source_item_id)
    if existing_crafting_slot:
        crafting_slot_repo.delete(craft_id, destination_item_id, source_item_id)
        return {"message": "Crafting slot deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Crafting slot not found")