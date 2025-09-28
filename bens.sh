fwks='
    aiohttp
    baize
    blacksheep
    django
    emmett
    falcon
    fastapi
    muffin
    quart
    sanic
    starlette
    tornado
    gin
'
OUT=report.txt
echo -n > $OUT # reset
docker compose stop
for fwk in $fwks; do
    # start
    docker compose up -d --build $fwk
    curl --retry-connrefused --retry 5 localhost:8000/route-1

    # bench
    python check.py || exit 1 # exit on error
    echo "svc:$fwk" | tee -a $OUT
    bash ben.sh | tee -a $OUT
    
    # stop
    docker compose stop $fwk
done
python report.py