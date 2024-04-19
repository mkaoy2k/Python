"""Examples of Sorting Customized Objects by its attributes
Assuming attributes are alphanumeric sortables
3 ways to sort an object
1. sorted() with key=user-defined-function
2. sorted() with key=lambda function
3. sorted() with key=attrgetter(), 'operator' Module required
"""

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},{})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl Washington', 37, 70000)
e2 = Employee('Sarah Dumbo', 29, 80000)
e3 = Employee('Michael Kao', 43, 90000)

print(f'Example of sorting an object:')
emp_li = [e1, e2, e3]
print(f'Original Emp List:\n{emp_li}\n')

def e_sort_name(emp):
    return emp.name


def e_sort_age(emp):
    return emp.age


def e_sort_salary(emp):
    return emp.salary

print(f'1. Sorted by user-defined function:')

s_emp_li = sorted(emp_li, key=e_sort_name)
print(f'===>Sorted by user-defined function w/ "name":')
print(f'{s_emp_li}\n')

s_emp_li2 = sorted(emp_li, key=e_sort_age)
print(f'===>Sorted by user-defined function w/ age:')
print(f'{s_emp_li2}\n')

s_emp_li3 = sorted(emp_li, key=e_sort_salary, reverse=True)
print('===>Sorted by user-defined function w/ salary in reverse:')
print(f'{s_emp_li3}\n')

# 2nd way to sort
print(f'2. Sorting object by lambda() function:')
s_emp_li4 = sorted(emp_li, key=lambda e: e.name, reverse=True)
print(f'===>By "name" in reverse order:')
print(f'{s_emp_li4}\n')

# 3rd way to sort
print(f'3. Sorting object by attrgetter() function:')
from operator import attrgetter

s_emp_li5 = sorted(emp_li, key=attrgetter('salary'), reverse=True)
print(f'===>By salary in reverse order:')
print(f'{s_emp_li5}\n')
