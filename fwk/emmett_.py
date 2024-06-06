from emmett import App

app = App(__name__)


@app.route("/hello/<str:name>")
async def hello(name: str):
    return f"hello, {name}"
