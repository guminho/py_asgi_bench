from litestar import Litestar, get


@get("/hello/{name:str}")
async def hello(name: str) -> str:
    return f"hello, {name}"


app = Litestar([hello])
