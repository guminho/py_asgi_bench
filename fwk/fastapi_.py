from common import NUM_ROUTE, build_html, build_json
from fastapi import FastAPI
from fastapi.responses import (
    HTMLResponse,
    ORJSONResponse,
    PlainTextResponse,
)

app = FastAPI()


# first add ten more routes to load routing system
# ------------------------------------------------
async def req_ok():
    return PlainTextResponse("ok")


for n in range(NUM_ROUTE):
    app.get(f"/route-{n}", name=f"req_ok_{n}")(req_ok)


# then prepare endpoints for the benchmark
# ----------------------------------------
@app.get("/html/{count}")
async def view_html(count: int):
    """Return HTML content"""
    content = await build_html(count)
    return HTMLResponse(content)


@app.get("/api/users/{user}/records/{record}")
async def view_api(user: int, record: int):
    """Return JSON content"""
    content = await build_json(user, record)
    return ORJSONResponse(content)
