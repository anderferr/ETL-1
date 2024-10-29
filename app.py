"""importando as libs"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """return value"""
    return {"message": "Hello World"}
