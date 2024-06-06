from muffin import Application

app = Application()


@app.route("/hello/{name}")
async def hello(request):
    name = request.path_params["name"]
    return f"hello, {name}"
