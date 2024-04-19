"""Example of sorting dictionaries using 'sortedcollections' module

    1. sort by key
    2. sort by value, assuming value are alphanumeric sortable"""
from sortedcollections import OrderedDict
from inspect import getmembers, isfunction, ismethod, isclass

# Display fuctions in OrderedDict package, using "inspect" module
print(f'Display functions in "OrderedDict" package')
for (name, member) in getmembers(OrderedDict, isfunction):
    if not name.startswith("_"):
        print(f'===>{name}')

# Display methods in OrderedDict package, using "inspect" module
print(f'Display methods in "OrderedDict" package')
for (name, member) in getmembers(OrderedDict, ismethod):
    if not name.startswith("_"):
        print(f'===>{name}')

# Display methods in OrderedDict package, using "inspect" module
print(f'Display classes in "OrderedDict" package')
for (name, member) in getmembers(OrderedDict, isclass):
    if not name.startswith("_"):
        print(f'===>{name}')

d = {"one": 1, "two": 2, "three": 3}
print(f'\nOriginal dictionary d is:\n{d}\n')

# dictionary sorted by key
d_key_sorted = {}
od = OrderedDict(sorted(d.items()))
print(f'OrderDict() returns a type of {type(od)}\n')
print(f'OrderedDict obj value is:\n{od}\n')

# Create a new dictionary from OrderdDict obj
# Processing (e.g. update a key's value) of an OrderedDict obj is the same as dictionary
od["one"] = 'aaa'
od.update(two='bbb')

for key, val in od.items():
    d_key_sorted[key] = val
    print(f'{key}:{val}')
print(f'New dictionary sorted by key is:\n{d_key_sorted}\n')

# dictionary sorted by value
d_val_sorted = {}
od = OrderedDict(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))

# Create a new dictionary from OrderedDict obj
for key, val in od.items():
    d_val_sorted[key] = val
    print(f'{key}:{val}')
print(f'New dictionary sorted by value is \n{d_val_sorted}\n')
