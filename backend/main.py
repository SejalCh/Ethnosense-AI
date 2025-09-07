from fastapi import FastAPI, HTTPException
from .data_loader import load_cultures

app = FastAPI(title="EthnoSense API", version="1.0")

cultures = load_cultures()

@app.get("/")
def root():
    return {"message": "Welcome to EthnoSense API"}

@app.get("/cultures")
def get_cultures():
    return cultures

@app.get("/cultures/{name}")
def get_culture(name: str):
    for c in cultures:
        if c["culture"].lower() == name.lower():
            return c
    raise HTTPException(status_code=404, detail="Culture not found")