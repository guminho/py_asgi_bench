import asyncio

NUM_ROUTE = 50


async def build_html(count: int) -> str:
    await asyncio.sleep(0.01)
    return f"<b>Incr {count + 1}</b>"


async def build_json(user: int, record: int) -> dict:
    await asyncio.sleep(0.01)
    return {
        "params": {
            "user": user + 1,
            "record": record + 1,
        },
        "data": "hello world",
    }
