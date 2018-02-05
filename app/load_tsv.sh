#!/usr/bin/env bash

STATS_TSV="/var/shared/stats.tsv"
LINES="$( wc -l ${STATS_TSV} | awk '{ print $1 }')"

echo "Inserting ${LINES} rows into clickhouse db:"
time clickhouse-client --host=ch-db --query="INSERT INTO stats_db.stats FORMAT TabSeparated" < ${STATS_TSV}
