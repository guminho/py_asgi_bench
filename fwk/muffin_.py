from muffin import Application, ResponseText

app = Application()


@app.route("/hello/{name}")
async def hello(request):
    name = request.path_params["name"]
    return ResponseText(f"hello, {name}")
