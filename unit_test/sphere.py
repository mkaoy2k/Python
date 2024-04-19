from math import pi
import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


import logging

logging.basicConfig(filename='sphere.log',
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def sphere_vol(r):
    logging.debug(f'{get_function_name()}: started.')
    if type(r) not in [int, float]:
        logging.error(
            f'\t{get_function_name()}: TypeError - The radius must be numeric type.')
        raise TypeError("The radius must be numeric type.")
    if r < 0:
        logging.error(
            f'\t{get_function_name()}: ValueError - The radius can not be negative.')
        raise ValueError("The radius can not be negative.")

    logging.debug(f'{get_function_name()}: ended normally.')

    return (4.0 / 3.0 * pi * (r**3))
