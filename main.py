from fastapi import FastAPI
import asyncio
import time
from random import randint

app = FastAPI()


@app.get("/")
async def root():
    # async wait for 5 seconds
    await asyncio.sleep(5)
    return {"magic_number": randint(1, 100)}


@app.get("/sync")
async def sync_endpoint():
    # sync wait for 5 seconds
    time.sleep(5)
    return {"magic_number": randint(1, 100)}
