import config

from clickhouse_driver import Client

c = Client(config.DB_CLICKHOUSE_HOST)
c.execute('DROP TABLE IF EXISTS stats_db.stats')
