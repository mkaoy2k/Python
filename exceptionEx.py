import logging
import time

# create logger
logging.basicConfig(filename='logger/problems.log',
                    level=logging.DEBUG)
logger = logging.getLogger()


def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required"""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"Time required for {path} = {dt}")
    return data


data = read_file_timed("Olisan.JPG")
