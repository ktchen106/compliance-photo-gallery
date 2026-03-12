from fastapi import FastAPI
from app.routers import property

app = FastAPI()

app.include_router(property.router)

@app.get("/")
def read_root():
    return {"message": "Compliance Photo Gallery API"}
