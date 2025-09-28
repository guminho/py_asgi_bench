from aiohttp.web import (
    Application,
    Request,
    Response,
    RouteTableDef,
    json_response,
)
from common import NUM_ROUTE, build_html, build_json

routes = RouteTableDef()


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok(request):
    return Response(text="ok")


for n in range(NUM_ROUTE):
    routes.get(f"/route-{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@routes.get(r"/html/{count:\d+}")
async def view_html(request: Request):
    """Return HTML content"""
    count = int(request.match_info["count"])
    content = await build_html(count)
    return Response(text=content, content_type="text/html")


@routes.get(r"/api/users/{user:\d+}/records/{record:\d+}")
async def view_api(request: Request):
    """Return JSON content"""
    user = int(request.match_info["user"])
    record = int(request.match_info["record"])
    content = await build_json(user, record)
    return json_response(content)


app = Application()
app.add_routes(routes)
