from math import pi

# function name macro
import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


# logging
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

log_file = 'circles.log'
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# calculate circle area function


def circle_area(r):
    if type(r) not in [int, float]:
        logger.debug(
            f'\t{get_function_name()} - TypeError')

        raise TypeError("The radius must be numeric type.")
    if r < 0:
        logger.debug(
            f'\t{get_function_name()} - ValueError')

        raise ValueError("The radius can not be negative.")
    return (pi * (r**2))


# main
if __name__ == '__main__':
    for i in range(5):
        print(f'radius={i}, circle area={circle_area(i)}')
