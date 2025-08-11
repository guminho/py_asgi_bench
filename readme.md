# Python ASGI Benchmark

## result
#### requests/sec:
```
mrhttp    :141686|#######################| 100/100
granian   :139493|#######################5| 98/100
graniana  : 88545|##############8         | 62/100
emmett    : 46631|#######6                | 32/100
uvicorn   : 45631|#######6                | 32/100
sanic     : 41217|######9                 | 29/100
muffin    : 35242|#####7                  | 24/100
blacksheep: 35189|#####7                  | 24/100
aiohttp   : 34769|#####7                  | 24/100
falcon    : 33477|#####5                  | 23/100
starlette : 30198|#####                   | 21/100
litestar  : 18878|###1                    | 13/100
robyn     : 16038|##6                     | 11/100
fastapi   : 15772|##6                     | 11/100
lilya     : 11558|##                       | 8/100
esmerald  :  9198|#5                       | 6/100
quart     :  8251|#2                       | 5/100
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