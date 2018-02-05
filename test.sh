#!/bin/bash

terminate() {
    kill ${profile_pid}
    exit 0
}

trap terminate SIGINT SIGTERM


docker-compose build

./profile.sh &
profile_pid=$!
echo "start logging PID = ${profile_pid}"

docker-compose run app python ./app/test_select.py

terminate
