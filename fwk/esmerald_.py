from esmerald import Esmerald
from esmerald.responses import PlainText

app = Esmerald()


@app.get("/hello/{name}")
async def hello(name: str) -> PlainText:
    return PlainText(f"hello, {name}")
