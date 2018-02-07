#!/usr/bin/env bash

STATS_TSV="/var/shared/stats-$1.tsv"
LINES="$( wc -l ${STATS_TSV} | awk '{ print $1 }')"

echo "Inserting ${LINES} rows into clickhouse db from $STATS_TSV:"
time clickhouse-client --host=ch-db --query="INSERT INTO stats_db.stats_$1 FORMAT TabSeparated" < ${STATS_TSV}
