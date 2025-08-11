from mrhttp import Request, app


@app.route("/hello/{}", _type="text")
async def hello(req: Request, name: str):
    return f"hello {name}"


app.run(port=8000)
