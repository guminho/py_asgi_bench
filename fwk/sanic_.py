from common import NUM_ROUTE, build_html, build_json
from sanic import Sanic
from sanic.response import html, json, text

app = Sanic("benchmark")


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok(request):
    return text("ok")


for n in range(NUM_ROUTE):
    app.route(f"/route-{n}", name=f"route-{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@app.route("/html/<count>")
async def view_html(request, count: int):
    """Return HTML content"""
    content = await build_html(count)
    return html(content)


@app.route("/api/users/<user>/records/<record>")
async def api(request, user: int, record: int):
    """Return JSON content"""
    content = await build_json(user, record)
    return json(content)
