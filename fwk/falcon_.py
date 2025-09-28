from json import dumps

from common import NUM_ROUTE, build_html, build_json
from falcon import MEDIA_HTML, MEDIA_TEXT
from falcon.asgi import App, Response


class HTMLView:
    """Return HTML content"""

    async def on_get(self, req, res: Response, count: int):
        res.content_type = MEDIA_HTML
        res.text = await build_html(count)


class APIView:
    """Return JSON content"""

    async def on_get(self, req, res: Response, user: int, record: int):
        content = await build_json(user, record)
        res.text = dumps(content, ensure_ascii=False, separators=(",", ":"))


app = App()


# first add ten more routes to load routing system
# ------------------------------------------------
class OKView:
    async def on_get(self, req, res: Response):
        res.content_type = MEDIA_TEXT
        res.text = "ok"


for n in range(NUM_ROUTE):
    app.add_route(f"/route-{n}", OKView())


# then prepare endpoints for the benchmark
# ----------------------------------------
app.add_route("/html/{count:int}", HTMLView())
app.add_route("/api/users/{user:int}/records/{record:int}", APIView())
