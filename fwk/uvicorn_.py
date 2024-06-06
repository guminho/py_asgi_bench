TYPE_START = "http.response.start"
TYPE_BODY = "http.response.body"

PLAINTEXT = dict(
    type=TYPE_START,
    status=200,
    headers=[(b"content-type", b"text/plain")],
)


async def app(scope: dict, recv, send):
    name = scope["path"].rsplit("/", 1)[1]
    await send(PLAINTEXT)
    await send(dict(type=TYPE_BODY, body=f"hello, {name}".encode()))
