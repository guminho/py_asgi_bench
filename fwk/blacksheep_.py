from blacksheep import Application, get
from blacksheep.server.responses import html, json, text
from common import NUM_ROUTE, build_html, build_json

app = Application()


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok():
    return text("ok")


for n in range(NUM_ROUTE):
    get(f"/route-{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@get("/html/{count}")
async def view_html(count: int):
    """Return HTML content"""
    content = await build_html(count)
    return html(content)


@get("/api/users/{user}/records/{record}")
async def view_api(user: int, record: int):
    """Return JSON content"""
    content = await build_json(user, record)
    return json(content)
