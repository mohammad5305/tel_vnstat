#!/bin/bash

set -euo pipefail

export INTERFACE=eth0
export TOKEN=""
export TG_CHAT_ID=""
export VNSTAT_LOG="plots/vnstat/vnstat.log"

set -x

vnstat -i $INTERFACE -b "$(date +%Y-%m-%d)" --json 'h' | jq -r ".interfaces[0].traffic.hour[] | (.time | (.hour | tostring) + \":\" + (.minute | tostring) ) + \" \" + ( ( ( (.rx + .tx) / 1024 ) / 1024 ) |round | tostring )" > $VNSTAT_LOG
docker run --rm --name ports_chart --workdir '/work' -v $(pwd)/plots/ports:/work remuslazar/gnuplot ./ports.p
docker run --rm --name vnstat_chart --workdir '/work' -v $(pwd)/plots/vnstat:/work remuslazar/gnuplot ./vnstat.p

python3 ./bot/main.py
