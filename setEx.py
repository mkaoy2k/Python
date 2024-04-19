# Set operations
cs_courses = {'History', 'Math', 'Physics', 'ComSci', 'Math'} # dup Math noticed
print('\nSet cs_courses (no duplicate):', cs_courses, '\n')

art_courses = {'History', 'Math', 'Art', 'Design'}

print('\nSet intersection:')
print(cs_courses.intersection(art_courses))

print('\nSet difference:')
print(cs_courses.difference(art_courses))

print('\nSet union:')
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This is NOT right! It's an empty Dictionary
empty_set = set() # only this valid, confusing!
 