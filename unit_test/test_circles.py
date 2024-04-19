import unittest
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

log_file = 'test_circles.log'
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Unit Test Cases
from circles import circle_area


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        logger.info(
            f'\t{get_function_name()} - Test area calculation when radius >= 0')

        # Test area calculation when radius >= 0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        logger.info(f'\t{get_function_name()} - Test value errors of radius')

        # Test value errors of radius
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        logger.info(f'\t{get_function_name()} - Test type errors of radius')

        # Test type errors of radius
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "string")


if __name__ == '__main__':
    logger.debug(f'Unit Testing of circles.py begins...')
    unittest.main()
