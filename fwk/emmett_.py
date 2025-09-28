from common import NUM_ROUTE, build_html, build_json
from emmett import App, response
from emmett.tools import service

app = App(__name__)


# first add ten more routes to load routing system
# ------------------------------------------------
@app.route([f"/route-{n}" for n in range(NUM_ROUTE)], methods="get")
async def req_ok():
    return "ok"


# then prepare endpoints for the benchmark
# ----------------------------------------
@app.route("/html/<int:count>", methods="get")
async def view_html(count):
    """Return HTML content"""
    response.content_type = "text/html"
    content = await build_html(count)
    return content


@app.route("/api/users/<int:user>/records/<int:record>", methods="get")
@service.json
async def api(user, record):
    """Return JSON content"""
    content = await build_json(user, record)
    return content
