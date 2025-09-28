from baize.asgi import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    Request,
    Response,
    Router,
    request_response,
)
from common import NUM_ROUTE, build_html, build_json

routes = []


# first add ten more routes to load routing system
# ------------------------------------------------
@request_response
async def req_ok(request):
    return PlainTextResponse("ok")


for n in range(NUM_ROUTE):
    routes.append((f"/route-{n}", req_ok))


# then prepare endpoints for the benchmark
# ----------------------------------------
@request_response
async def view_html(request: Request) -> Response:
    """Return HTML content"""
    count = request.path_params["count"]
    content = await build_html(count)
    return HTMLResponse(content)


@request_response
async def view_api(request: Request) -> Response:
    """Return JSON content."""
    user = request.path_params["user"]
    record = request.path_params["record"]
    content = await build_json(user, record)

    return JSONResponse(content)


app = Router(
    *routes,
    ("/html/{count:int}", view_html),
    ("/api/users/{user:int}/records/{record:int}", view_api),
)
