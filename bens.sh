fwks='
    mrhttp
    granian
    graniana
    uvicorn
    emmett
    blacksheep
    sanic
    aiohttp
    falcon
    muffin
    starlette
    robyn
    fastapi
'
OUT=report.txt
echo -n > $OUT # reset

for fwk in $fwks; do
    # start
    docker-compose build -q $fwk
    docker-compose up -d $fwk
    sleep 1.5
    docker-compose ps --format 'table {{.Service}}' | tail -n1
    curl localhost:8000/hello/x && echo
    
    # bench
    echo -n "$fwk:" >> $OUT
    bash ben.sh | tail -2 | head -1 | tr -s ' ' | cut -d' ' -f2 >> $OUT
    
    # stop
    docker-compose stop $fwk
    sleep 1
    echo
done