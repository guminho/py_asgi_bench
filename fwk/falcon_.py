from falcon import HTTP_200, MEDIA_TEXT, Request, Response
from falcon.asgi import App


class Hello:
    async def on_get(self, req: Request, res: Response, name: str):
        res.status = HTTP_200
        res.content_type = MEDIA_TEXT
        res.text = f"hello, {name}"


app = App()
app.add_route("/hello/{name}", Hello())
