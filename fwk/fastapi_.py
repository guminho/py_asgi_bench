from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/hello/{name}")
async def hello(name: str):
    return PlainTextResponse(f"hello, {name}")
