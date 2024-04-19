import sys

print('Python sys.version:\n{}\n'.format(sys.version))

print('Python sys.executable:\n{}\n'.format(sys.executable))


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Michael', 'Kao')
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
