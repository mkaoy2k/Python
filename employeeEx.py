import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

log_file = 'logger/employee.log'
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(
            'Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


if __name__ == '__main__':

    # Test logging messages
    logger.debug("This is a harmless debug message.")
    logger.info("Just for your info.")
    logger.warning("I am warning you.")
    logger.error("Did you just try to divide by zero?")
    logger.critical("The system can not access Internet.")
    print(f'Check logging data at the end of {log_file} file...\n')
    print(f'''Note:
    1. No debugging messages since level is set at least 'INFO'
    2. logging file will be starting as a new file 'w' mode,
    as opposed to append by default
    ''')
