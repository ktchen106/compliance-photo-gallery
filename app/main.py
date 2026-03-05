from fastapi import FastAPI

app = FastAPI(title="Compliance Photo Gallery")

@app.get("/")
def read_root():
    return {"Hello": "World"}
