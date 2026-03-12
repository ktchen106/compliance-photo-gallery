from fastapi import FastAPI
from app.routers import property

app = FastAPI()

app.include_router(property.router)

@app.get("/")
def read_root():
    return {"message": "Compliance Photo Gallery API"}

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "0.1.0"}
