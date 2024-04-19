import xml.etree.ElementTree as ET
"""This is an example of inspecting classes and functions of 'xml' module 
using 'inspect' module
"""

# Using 'inspect' Module to display related classes, functions etc
from inspect import getmembers, isfunction, isclass


# Display classes in ET package, using "inspect" module
print(f'Display classes in "ET" package')
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(f'===>{name}')
print()

# Display fuctions in ET package, using "inspect" module
print(f'Display functions in "ET" package')
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(f'===>{name}')
print()
