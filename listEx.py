# List operations
courses = ['History', 'Physics', 'ComSci']
print('List of courses:', courses, '\n')
print('   The fist element of list begins with idx zero: ', courses[0])
print('   The last element of list can be retrieved with idx -1:', courses[-1])
print('   The range of list is from element 0 until 2 (not including 2):\n     ',
      courses[:2])
print('   The range of last two elements of the list:\n     ', courses[-2:])
print('   The length of list:', len(courses), '\n')

courses_2 = ['Art', 'Education']
print('List of another courses:', courses_2, '\n')

print('To insert a course: Math, on idx 1, list begins with zero')
courses.insert(1, 'Math')
print('List of courses:\n  ', courses, '\n')

print('To insert a course_2, which is an another list')
courses.insert(0, courses_2)
print('List of courses:\n  ', courses, '\n')

print('To append a course: Art, to the last of list')
courses.append(courses_2)
print('List of courses:\n  ', courses, '\n')

print('To pop the last element of list')
courses.pop()
print('List of courses:\n  ', courses, '\n')

print('To remove an element from the list, say course_2')
courses.remove(courses_2)
print('List of courses:\n  ', courses, '\n')

print('To insert only course elements contained in the course_2 list')
courses.extend(courses_2)
print('List of courses:\n  ', courses, '\n')

print('To remove an elelment: course, Art')
courses.remove('Art')
print('List of courses:\n  ', courses, '\n')

# Reversing List: 3 ways to do this
# 1. Using slicing operator to reverse the elements of the list
print(f'1. Using slicing operator to reverse the elements of the list...')
reversed_courses = courses[::-1]
print(f'List of reversed courses:\n  {reversed_courses}\n')

# 2. Using reverse() method to reverse the elements of the list
print(f'2. Using reverse() method to reverse the elements of the list...')
reversed_courses.reverse()
print(f'Reverse the reversed courses:\n  {reversed_courses}')
print(f'List of original courses:\n  {courses}\n')

# 3. Accessing elements in reversed order, using reversed() function
print(f'3. Accessing elements in reversed order, using reversed()...')
for ele in reversed(courses):
    print(f'  {ele}')

print()

# Sorting list
nums = [1, 5, 3, 7, 9]

# Sort numbers
print('The list of numbers:', nums, '\n')
print('   Minimum of list numbers:', min(nums), '\n')
print('   Maximum of list numbers:', max(nums), '\n')
print('   Sum of list numbers:', sum(nums), '\n')

nums.sort()
print('Sorting numbers in accendng order:\n  ', nums, '\n')

nums.sort(reverse=True)
print('Sorting numbers in deccendng order:\n  ', nums, '\n')

# keep the original intact
print('Keep the original list')
sorted_courses = sorted(courses)
print('List of courses:\n  ', courses, '\n')
print('List of sorted courses:\n  ', sorted_courses, '\n')

# More operations of list
print('Finding a course, ComSci, if it is in the list course: ',
      'ComSci' in courses, '\n')
print('   locating its index in the list: ', courses.index('ComSci'), '\n')
print('Finding a course, Art, if it is in the list course: ', 'Art' in courses, '\n')

# Looping thru the list
print('\nThe list of courses one per line:')
for course in courses:
    print(course)

print('\nThe list of courses one pair per line:')
for index, course in enumerate(courses):
    print(index, course)

print('\nThe list of courses one pair (index from 1) per line:')
for index, course in enumerate(courses, start=1):
    print(index, course)

# Joining the list
print('\nJoining ", " b/t the list of courses:\n  ', ', '.join(courses))

courses_str = ' - '.join(courses)
print('\nJoining " - " b/t the list of courses:\n  ', courses_str)

# Spliting the list
new_list = courses_str.split(' - ')
print('\nSpliting back to a list by " - ":\n  ', new_list)
