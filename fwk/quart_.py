from quart import Quart

app = Quart(__name__)


@app.route("/hello/<name>")
async def hello(name: str):
    return f"hello, {name}"
