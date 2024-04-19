import unittest
from unittest.mock import patch

import traceback


def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]


from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'\t{get_function_name()}')

    @classmethod
    def tearDownClass(cls):
        print(f'\t{get_function_name()}')

    def setUp(self):
        print(f'\t{get_function_name()}')
        self.emp_1 = Employee('Michael', 'Kao', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        print(f'\t{get_function_name()}')

    def test_email(self):
        print(f'\t{get_function_name()}')
        self.assertEqual(self.emp_1.email, 'Michael.Kao@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Kao@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print(f'\t{get_function_name()}')
        self.assertEqual(self.emp_1.fullname, 'Michael Kao')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Kao')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print(f'\t{get_function_name()}')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        print(f'\t{get_function_name()}')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Kao/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


print(f'Testing employee.py\n')

if __name__ == '__main__':
    unittest.main()
