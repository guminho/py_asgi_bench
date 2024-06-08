fwks='
    aiohttp
    blacksheep
    emmett
    fastapi
    muffin
    robyn
    sanic
    starlette
    granian
    uvicorn
'
OUT=report.txt
echo -n > $OUT # reset

for fwk in $fwks; do
    # start
    docker compose build -q $fwk
    docker compose up -d $fwk
    sleep 1
    curl localhost:8000/hello/x
    
    # bench
    echo -n "$fwk:" >> $OUT
    bash ben.sh | tail -2 | head -1 | cut -d" " -f3 >> $OUT
    
    # stop
    docker compose stop $fwk
    sleep 1
    echo
done