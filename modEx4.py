# caller of my_module
#

from my_module import find_index, test
# or import everything from my_module, as follows:
#from my_module import *


courses = ['History', 'Math', 'Physics', 'ComSci']

index = find_index(courses, 'Math')
print('   index found for "Math":', index)
print('   accessing "test" variable in my_module:', test)

# To inquire the search path for a module, defined in PYTHONPATH env as well
print('\nTo inquire the search path for a module...')
import sys
print(sys.path)

#import random
print('\nTo import random module...')
import random

for course in courses:
	random_course = random.choice(courses)
	print('   random course selected:', random_course)