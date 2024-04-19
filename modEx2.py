# caller of my_module
#

import my_module as mm

courses = ['History', 'Math', 'Physics', 'ComSci']

index = mm.find_index(courses, 'Math')
print(index)
