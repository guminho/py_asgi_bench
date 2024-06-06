from blacksheep import Application, get, text

app = Application()


@get("/hello/{name}")
async def hello(name: str):
    return text(f"hello, {name}")
