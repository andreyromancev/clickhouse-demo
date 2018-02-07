import os
import subprocess

import config
import generate_data

ROWS = 50 * 1000 * 1000
CHUNK = 3 * 1000


def generate():
    generate_data.generate_data_flat('/var/shared/stats-flat.tsv', ROWS, CHUNK)
    generate_data.generate_data_null('/var/shared/stats-null.tsv', ROWS, CHUNK)
    generate_data.generate_data_collapse('/var/shared/stats-collapse.tsv', ROWS, CHUNK)


def fill_tables():
    subprocess.call([os.path.join(config.BASE_DIR, 'load_tsv.sh'), 'flat'])
    subprocess.call([os.path.join(config.BASE_DIR, 'load_tsv.sh'), 'null'])
    subprocess.call([os.path.join(config.BASE_DIR, 'load_tsv.sh'), 'collapse'])


generate()
fill_tables()
