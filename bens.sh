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
for fwk in $fwks; do
    echo "- $fwk:"
    docker compose build -q $fwk
    docker compose up -d $fwk
    sleep 1
    
    curl localhost:8000/hello/x
    echo    
    bash ben.sh | tail -2 | head -1
    
    docker compose stop $fwk
    echo
done