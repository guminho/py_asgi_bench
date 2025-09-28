from common import NUM_ROUTE, build_html, build_json
from quart import Quart, Response

app = Quart(__name__)


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok():
    return Response("ok", content_type="text/plain")


for n in range(NUM_ROUTE):
    app.route(f"/route-{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@app.route("/html/<int:count>")
async def hello(count):
    """Return HTML content."""
    content = await build_html(count)
    return Response(content, content_type="text/html")


@app.route("/api/users/<int:user>/records/<int:record>")
async def api(user, record):
    """Return JSON content."""
    content = await build_json(user, record)
    return content
