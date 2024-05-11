from dotenv import load_dotenv

from src.middleware.setup import setup_middleware
load_dotenv()


from fastapi import FastAPI
import uvicorn

from src.router.api_router import setup_routes

description = """
AlbionMC API helps you manage the AlbionMC Database. 🚀

## Items

You will be able to manage **items**.

## Crafting Slots

You will be able to manage **crafting slots**.

## Item Prices

You will be able to manage **item prices**.

## Data Sources

You will be able to manage **data sources**.

"""
app = FastAPI(
    title="AlbionMC",
    description=description,
    summary="Albion Market Calculator.",
    version="0.0.1",
    terms_of_service="https://github.com/jtomaspm/AlbionMC/tree/main",
    contact={
        "name": "Github",
        "url": "https://github.com/jtomaspm/AlbionMC/tree/main",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },)


setup_routes(app, '/api')
setup_middleware(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)