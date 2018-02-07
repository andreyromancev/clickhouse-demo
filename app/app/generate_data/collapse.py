import csv
import datetime
import random
import time


def get_chunk_row(index, time_from, time_step):
    current_time = time_from + index * time_step
    dt = datetime.datetime.fromtimestamp(current_time)
    return [
        random.randint(0, 1000),
        'L',
        random.randint(0, 1000),
        random.randint(0, 100),

        current_time,
        dt.date(),
        dt.year,
        (dt.month - 1) // 3,
        dt.month,
        dt.hour,

        10000,
        10000,
        10000,
        10000,

        0,
        0,

        '\N',
        '\N',

        1000,
        1000,
        1000,
        1000,
        1000,
        1000,
        1000,
        1000,
        1000,
        1000,
        1000,

        100,
        100,
        100,
        100,
        100,
        100,
    ]


def get_single_row(index, time_from, time_step):
    current_time = time_from + index * time_step
    dt = datetime.datetime.fromtimestamp(current_time)
    return [
        random.randint(0, 1000),
        'L',
        random.randint(0, 1000),
        random.randint(0, 100),

        current_time,
        dt.date(),
        dt.year,
        (dt.month - 1) // 3,
        dt.month,
        dt.hour,

        0,
        0,
        0,
        0,

        1,
        0,

        'M',
        'I',

        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,

        0,
        0,
        0,
        0,
        0,
        0,
    ]


def generate_data_collapse(filepath, rows, chunk):
    print('Generating data for {} rows...'.format(rows))
    with open(filepath, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')

        time_to = int(time.time())
        time_from = int(time_to - datetime.timedelta(days=365).total_seconds())
        time_step = int((time_to - time_from) / rows)
        i = 0
        while i <= rows:
            if i % chunk == 0:
                w.writerow(get_chunk_row(i, time_from, time_step))

            if i % 100 < 15:
                w.writerow(get_single_row(i, time_from, time_step))

            i += 1
            if i % 100000 == 0:
                print('{}%'.format(int(float(i) / rows * 100)))

    print('Generation successful')
