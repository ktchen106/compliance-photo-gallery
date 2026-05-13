from fastapi import FastAPI
from app.routers import property

app = FastAPI(
    title="Compliance Photo Gallery",
    description="API for managing properties and their compliance photos.",
    version="1.0.0"
)

app.include_router(property.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Compliance Photo Gallery API"}
