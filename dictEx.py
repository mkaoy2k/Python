"""Examples of Dictionary
    There are 3 methods to loop thru a dictionary:
    1. items()
    2. keys()
    3. values()
"""
# Dictionaries - Working with Key_Value Pairs
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'ComSci']}
print('Dictionary student initialized:', student)

print('===>Accessing with key="name":\n\t', student['name'])
print('===>Accessing all keys:\n\t', student.keys())
print('===>Accessing all valuess:\n\t', student.values())
print('===>Accessing all key-value pairs:\n\t', student.items())
print('===>Inquire the size of Dictionary:\n\t', len(student))

# Looping thru Dictionary
print('===>Key-value pairs with items() method are listed below:')
for key, value in student.items():
    print(f'\t"{key}":{value}')

# To avoid a KeyError from Python, catching error when key not found
print('===>Accessing with non-existent key="phone":\n\t',
      student.get('phone', 'Not Found!'))

# To insert a value with a new key
student['phone'] = '555-5555'
print('Dictionary student inserted "555-5555" with a new key="phone":\n\t', student)

print('===>Accessing with key="phone":\n\t',
      student.get('phone', 'Not Found!'))

# To update a key with a new value
student['name'] = 'Jane'
print('Dictionary student updated value "Jane" with key="name":\n\t', student)

# To update multiple keys with values
student.update({'name': 'Jim', 'age': 23, 'phone': '888-8888'})
print('Dictionary student updated multiple values:\n\t', student)

# To delete a key-value pair from Dictionary
del student['phone']
print('Dictionary student key-value "phone" deleted:\n\t', student)

# To pop a key-value pair from Dictionary and the value retrieved
age = student.pop('age')
print('Dictionary student key-value "age" popped:\n\t', student)
print('===>Value of Key="age" popped:', age)
