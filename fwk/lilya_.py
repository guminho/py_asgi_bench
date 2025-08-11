from lilya.apps import Lilya
from lilya.responses import PlainText

app = Lilya()


@app.get("/hello/{name}")
async def hello(name: str):
    return PlainText(f"hello, {name}")
