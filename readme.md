# Python ASGI Benchmark

## result
#### requests/sec:
```
granian   :134848|#######################| 100/100
mrhttp    :125493|######################3 | 93/100
graniana  : 76895|#############6          | 57/100
emmett    : 46061|########1               | 34/100
uvicorn   : 38833|######7                 | 28/100
sanic     : 33877|######                  | 25/100
aiohttp   : 31518|#####5                  | 23/100
muffin    : 31332|#####5                  | 23/100
blacksheep: 31192|#####5                  | 23/100
falcon    : 29543|#####                   | 21/100
starlette : 26753|####5                   | 19/100
robyn     : 16882|##8                     | 12/100
fastapi   : 16717|##8                     | 12/100
```

## how-to-run
### prerequisite
- install [wg/wrk](https://github.com/wg/wrk)

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

## ref
- [techempower.com/benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=fd4f1f27-72cd-4e89-92c6-0d965fadb733&hw=ph&test=update&l=zijocf-6bi)