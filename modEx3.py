# caller of my_module
#

# test within my_module still accessible
from my_module import find_index as fi, test


courses = ['History', 'Math', 'Physics', 'ComSci']

index = fi(courses, 'Math')
print(index)
print(test)
