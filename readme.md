# Python ASGI Benchmark

## result
#### requests/sec:
```
granian   |█████████████████████████████████████████| 118783.02
emmett    |███████████████████▋                     | 55682.74
uvicorn   |████████████████▊                        | 46718.21
blacksheep|█████████████▍                           | 37922.09
muffin    |████████████▌                            | 35245.47
sanic     |███████████▊                             | 32851.52
robyn     |██████████▌                              | 28943.69
starlette |█████████▋                               | 26534.6
aiohttp   |███████▉                                 | 22527.1
fastapi   |█████▌                                   | 15177.57
```

## how-to-run
#### one-click
```bash
bash bens.sh
```

#### detail
```bash
# deploy 1 of the servers
docker-compose up -d --build aiohttp
docker-compose up -d --build blacksheep
docker-compose up -d --build emmett
...

# client
curl localhost:8000/hello/x

# bench
bash ben.sh
```

