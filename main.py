from fastapi import FastAPI
import asyncio
from random import randint

app = FastAPI()


@app.get("/")
async def root():
    # async wait for 5 seconds
    await asyncio.sleep(5)
    return {"magic_number": randint(1, 100)}
