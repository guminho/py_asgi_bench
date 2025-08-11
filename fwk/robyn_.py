from robyn import Request, Robyn

app = Robyn(__file__)


@app.get("/hello/:name")
async def hello(request: Request):
    name = request.path_params["name"]
    return f"hello, {name}"


if __name__ == "__main__":
    app.start(port=8000)
