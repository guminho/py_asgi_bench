import uvloop
from common import NUM_ROUTE, build_html, build_json
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import access_log
from tornado.web import Application, RequestHandler, url


class ReqOk(RequestHandler):
    async def get(self):
        self.set_header("content-type", "text/plain")
        self.write("ok")


class HTML(RequestHandler):
    async def get(self, count: str):
        content = await build_html(int(count))
        self.write(content)


class API(RequestHandler):
    async def get(self, user: str, record: str):
        content = await build_json(int(user), int(record))
        self.write(content)


handlers = [
    *[url(f"/route-{n}", ReqOk) for n in range(NUM_ROUTE)],
    url("/html/([0-9]+)", HTML),
    url("/api/users/([0-9]+)/records/([0-9]+)", API),
]
app = Application(handlers)


# Start the application
if __name__ == "__main__":
    uvloop.install()
    server: HTTPServer = HTTPServer(app)
    server.bind(8000, reuse_port=True)
    server.start()
    access_log.setLevel("ERROR")
    IOLoop.current().start()
