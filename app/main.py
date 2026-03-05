from fastapi import FastAPI
from app.routers.property import router as property_router

app = FastAPI(title="Compliance Photo Gallery")

app.include_router(property_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
