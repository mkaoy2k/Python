"""Performance comparison among INSERT SQL command into Postgresql DB
when 1-record insert vs multiple-records at a time.
"""

# Postgresql Database module
import psycopg2

import time
from dotenv import load_dotenv
import os


# Number of rows to asdd in each batch
n = 10_000

# Generate single INSERT INTO statement
single_insert = """INSERT INTO post (user_id, post_text)
    VALUES (1, 'Hello World!');"""

# Generate one BIG INSERT statement
big_insert = "INSERT INTO post(user_id, post_text) VALUES "
for i in range(n):
    big_insert += "(1, 'Hello World!'),"
big_insert = big_insert.strip(',') + ';'    # replace trailing ',' with ';'

# Initialize login parms from files
path_dir = 'sample'  # relative to the current dir
file_db = f'{path_dir}/dbname.txt'
file_user = f'{path_dir}/username.txt'

# Load environment variables
load_dotenv()
pw = os.getenv('DB_PW')
if not pw:
    raise ValueError("環境變數 DB_PW 未設定")

with open(file_db, 'r') as f:
    db = f.read()
with open(file_user, 'r') as f:
    username = f.read()

# Connect to DB & create cursor
connect_info = f'dbname={db} user={username} password={pw}'

with psycopg2.connect(connect_info) as conn:
    with conn.cursor() as cur:

        # Time 1-record INSERT at a time
        start_time = time.time()
        for i in range(n):
            cur.execute(single_insert)
        conn.commit()
        stop_time = time.time()
        single_performance = stop_time - start_time
        print(f'Individual INSERT took {single_performance} seconds.')

        # Time the BIG INSERT
        start_time = time.time()
        cur.execute(big_insert)
        conn.commit()
        stop_time = time.time()
        batch_performance = stop_time - start_time
        print(f'Big INSERT took {batch_performance} seconds.')

ratio_SvsB = single_performance / batch_performance
print(
    f'===> Single INSERT over big Batch, took {ratio_SvsB:3.1f} times longer\n')
