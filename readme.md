# Python ASGI Benchmark

## result
#### requests/sec:
```
granian   :118783|#######################| 100/100
emmett    : 55682|###########             | 46/100
uvicorn   : 46718|#########3              | 39/100
blacksheep: 37922|#######4                | 31/100
muffin    : 35245|######9                 | 29/100
sanic     : 32851|######4                 | 27/100
robyn     : 28943|#####7                  | 24/100
starlette : 26534|#####2                  | 22/100
aiohttp   : 22527|####3                   | 18/100
fastapi   : 15177|##8                     | 12/100
```

## how-to-run
#### quick-run
```bash
bash bens.sh
python report.py
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