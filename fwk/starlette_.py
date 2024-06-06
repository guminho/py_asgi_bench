from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def hello(request: Request):
    name = request.path_params["name"]
    return PlainTextResponse(f"hello, {name}")


routes = [Route("/hello/{name}", hello)]
app = Starlette(routes=routes)
