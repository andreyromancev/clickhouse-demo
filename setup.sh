#!/usr/bin/env bash

docker-compose build
docker-compose run app python ./app/drop_tables.py
docker-compose run app python ./app/create_tables.py
docker-compose run app python ./app/fill_tables.py
