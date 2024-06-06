from sanic import Sanic, Request, text

app = Sanic("App")


@app.get("/hello/<name>")
async def hello(request: Request, name: str):
    return text(f"hello, {name}")
