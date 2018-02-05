FROM python:2.7

ARG repository="deb https://repo.yandex.ru/clickhouse/xenial/ dists/stable/main/binary-amd64/"
ARG version=\*

RUN apt-get update && \
    apt-get install -y apt-transport-https tzdata && \
    apt-get install -y time && \
    mkdir -p /etc/apt/sources.list.d && \
    echo $repository | tee /etc/apt/sources.list.d/clickhouse.list && \
    apt-get update && \
    apt-get install --allow-unauthenticated -y clickhouse-client=$version locales && \
    rm -rf /var/lib/apt/lists/* /var/cache/debconf && \
    apt-get clean

WORKDIR /var/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
