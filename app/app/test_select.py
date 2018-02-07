import os

import config

from clickhouse_driver import Client


c = Client(config.DB_CLICKHOUSE_HOST)


def test_aggregate():
    c.execute("""
        SELECT
            project_id,
            sum(clicked_total) as clicked,
            sum(viewed) as viewed,
            sum(sent) as sent,
            clicked / sent,
            viewed / sent,
            sum(opened_total) as opened_total,
            sum(opened_dev_pc) / opened_total,
            sum(opened_dev_mobile) / opened_total,
            sum(opened_dev_tablet) / opened_total,
            sum(opened_dev_other) / opened_total,
            sum(stop_total)
        FROM stats_db.stats
        GROUP BY project_id WITH TOTALS
        ORDER BY project_id
    """)


def test_partition():
    c.execute("""
        SELECT
            date,
            sum(clicked_total) as clicked,
            sum(viewed) as viewed,
            sum(sent) as sent,
            clicked / sent,
            viewed / sent,
            sum(opened_total) as opened_total,
            sum(opened_dev_pc) / opened_total,
            sum(opened_dev_mobile) / opened_total,
            sum(opened_dev_tablet) / opened_total,
            sum(opened_dev_other) / opened_total,
            sum(stop_total)
        FROM stats_db.stats
        GROUP BY project_id, date WITH TOTALS
        ORDER BY project_id, date
    """)


for i in range(0, 10):
    test_aggregate()
    test_partition()
