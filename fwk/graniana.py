RESP_START = "http.response.start"
RESP_BODY = "http.response.body"
PLAINTEXT = (b"content-type", b"text/plain")


async def app(scope: dict, receive, send):
    name = scope["path"].rsplit("/", 1)[1]
    await send({"type": RESP_START, "status": 200, "headers": [PLAINTEXT]})
    await send({"type": RESP_BODY, "body": f"hello, {name}".encode()})
