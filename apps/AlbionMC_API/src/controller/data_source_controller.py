from dataclasses import asdict
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from src.core.entities.data_source import DataSource
from src.repository.data_source_repository import DataSourceRepository

data_source_router = APIRouter(prefix="/data_sources")

from src.dependencies import configure_injector
injector = configure_injector()

@data_source_router.get("/")
def get_data_sources(data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    return [asdict(ds) for ds in data_source_repo.get_all()]

@data_source_router.get("/{data_source_id}")
def get_data_source(data_source_id: int, data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    data_source = data_source_repo.get(data_source_id)
    if data_source:
        return asdict(data_source)
    else:
        raise HTTPException(status_code=404, detail="Data source not found")

@data_source_router.post("/")
def create_data_source(data_source: DataSource, data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    data_source_repo.new(data_source)
    return {"message": "Data source created successfully"}

@data_source_router.post("/batch")
def create_data_sources(data_sources: List[DataSource], data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    try:
        data_source_repo.new_batch(data_sources)
        return {"message": "Data sources created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@data_source_router.put("/{data_source_id}")
def update_data_source(data_source_id: int, data_source: DataSource, data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    existing_data_source = data_source_repo.get(data_source_id)
    if existing_data_source:
        data_source.id = data_source_id
        data_source_repo.update(data_source)
        return {"message": "Data source updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data source not found")

@data_source_router.delete("/{data_source_id}")
def delete_data_source(data_source_id: int, data_source_repo: DataSourceRepository = Depends(lambda: injector.get(DataSourceRepository))):
    existing_data_source = data_source_repo.get(data_source_id)
    if existing_data_source:
        data_source_repo.delete(data_source_id)
        return {"message": "Data source deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data source not found")