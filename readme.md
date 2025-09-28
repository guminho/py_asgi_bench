# Python ASGI Benchmark

inspired by [klen.github.io/py-frameworks-bench](https://klen.github.io/py-frameworks-bench/)
updated: 2025-09-28

A simple benchmark for python async frameworks. Most of the frameworks are ASGI-compatible.

## result
#### requests/sec:
Note: Each endpoint has a sleep of 10ms to represent some IO processing
```
 frameworks  latency      rps
gin        : 10.83ms:  5889.2|##############################|100.0
emmett     : 11.03ms:  5791.8|############################# | 98.3
starlette  : 11.15ms:  5725.6|############################# | 97.2
fastapi    : 11.31ms:  5647.9|############################  | 95.9
falcon     : 11.55ms:  5524.6|############################  | 93.8
sanic      : 11.62ms:  5489.8|###########################   | 93.2
blacksheep : 11.74ms:  5440.4|###########################   | 92.4
aiohttp    : 11.76ms:  5425.6|###########################   | 92.1
muffin     : 11.84ms:  5390.3|###########################   | 91.5
baize      : 11.86ms:  5381.7|###########################   | 91.4
quart      : 12.83ms:  4976.9|#########################     | 84.5
tornado    : 16.35ms:  3909.1|###################           | 66.4
django     : 31.27ms:  2045.0|##########                    | 34.7
```

## how-to-run
### prerequisite
- install [wg/wrk](https://github.com/wg/wrk)

#### quick-run
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
curl localhost:8000/html/1

# bench
bash ben.sh
```

## ref
- [techempower.com/benchmarks](https://www.techempower.com/benchmarks/#section=test&runid=fd4f1f27-72cd-4e89-92c6-0d965fadb733&hw=ph&test=update&l=zijocf-6bi)