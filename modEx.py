# caller of my_module
#

import my_module

courses = ['History', 'Math', 'Physics', 'ComSci']

index = my_module.find_index(courses, 'Math')
print(index)
