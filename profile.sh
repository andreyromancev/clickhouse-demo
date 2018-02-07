#!/bin/bash

while :
do
    docker stats --no-stream clickhouse_ch-db_1 >> .data/container-stats-$1.txt
    sleep 1
done
