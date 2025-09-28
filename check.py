import httpx

from fwk.common import NUM_ROUTE

with httpx.Client(base_url="http://localhost:8000") as cli:
    for n in range(NUM_ROUTE):
        res = cli.get(f"/route-{n}")
        assert res.status_code == 200
        assert "text/plain" in res.headers["content-type"]
        assert res.text == "ok"

    res = cli.get("/html/1")
    assert res.status_code == 200
    assert "text/html" in res.headers["content-type"]
    assert res.text == "<b>Incr 2</b>"

    res = cli.get("/api/users/1/records/1")
    assert res.status_code == 200
    assert "application/json" in res.headers["content-type"]
    assert res.json()["params"]["record"] == 2

print("ok")
