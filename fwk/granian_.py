from granian.rsgi import HTTPProtocol, Scope

PLAINTEXT = ("content-type", "text/plain")


async def app(scope: Scope, proto: HTTPProtocol):
    name = scope.path.rsplit("/", 1)[1]
    proto.response_str(200, [PLAINTEXT], f"hello, {name}")
