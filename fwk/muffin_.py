from common import NUM_ROUTE, build_html, build_json
from muffin import Application, Request, ResponseHTML, ResponseJSON, ResponseText

app = Application()


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok(request):
    return ResponseText("ok")


for n in range(NUM_ROUTE):
    app.route(f"/route-{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@app.route("/html/{count:int}")
async def html(request: Request):
    """Return HTML content"""
    count = request.path_params["count"]
    content = await build_html(count)
    return ResponseHTML(content)


@app.route("/api/users/{user:int}/records/{record:int}")
async def api(request):
    """Return JSON content"""
    user = request.path_params["user"]
    record = request.path_params["record"]
    content = await build_json(user, record)
    return ResponseJSON(content)
