from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/hello/{name}")
async def hello(request: web.Request):
    name = request.match_info["name"]
    return web.Response(text=f"hello, {name}")


app = web.Application()
app.add_routes(routes)
