from sanic import Request, Sanic, text

app = Sanic("App")


@app.get("/hello/<name>")
async def hello(request: Request, name: str):
    return text(f"hello, {name}")
