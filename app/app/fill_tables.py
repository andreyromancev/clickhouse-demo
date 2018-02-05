import os
import csv
import datetime
import random
import subprocess
import time

import config

STAT_ROWS = 50 * 1000 * 1000

MESSAGE_TYPES = ('L', 'S', 'G')
PROJECT_IDS = range(0, 100)
MESSAGE_IDS = range(0, 1000)
POST_IDS = range(0, 100)


def generate_data():
    print('Generating data for {} rows...'.format(STAT_ROWS))
    with open('/var/shared/stats.tsv', 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')

        time_to = int(time.time())
        time_from = int(time_to - datetime.timedelta(days=365).total_seconds())
        time_step = int((time_to - time_from) / STAT_ROWS)
        i = 0
        while i <= STAT_ROWS:
            current_time = time_from + i * time_step
            dt = datetime.datetime.fromtimestamp(current_time)
            w.writerow([
                random.choice(PROJECT_IDS),
                random.choice(MESSAGE_TYPES),
                random.choice(MESSAGE_IDS),
                random.choice(POST_IDS) if random.randint(0, 100) < 90 else '\N',

                current_time,
                dt.date(),
                dt.year,
                (dt.month - 1) // 3,
                dt.month,
                dt.hour,

                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),

                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),

                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),

                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),
                random.randint(0, 100000),

                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
            ])
            i += 1
            if i % 100000 == 0:
                print('{}%'.format(int(float(i) / STAT_ROWS * 100)))


def fill_tables():
    subprocess.call(os.path.join(config.BASE_DIR, 'load_tsv.sh'))


generate_data()
fill_tables()
