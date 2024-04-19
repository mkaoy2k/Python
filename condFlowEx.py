# Comparisons:
#
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=

language = 'Java'

if language == 'Python':
	print('Language is Python\n')
elif language == 'Java':
	print('Language is Java\n')
elif language == 'JavaScript':
	print('Language is JavaScript\n')
else:
	print('No match\n')

# Conditional expression 
# and
# or
# not

user = 'Admin'
logged_in = True

if not logged_in:
	print('Please log in\n') 
else:
	print('Welcome\n')

if user == 'Admin' and logged_in:
	print('Admin Page\n')
else:
	print('Bad Creds\n')

# Object Identity is

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print('id(a)=', id(a))
print('id(b)=', id(b))
print('id(c)=', id(c))

# checking equality of content
print('a == c?', a == c)

# checking equality of id
# same as id(a) == id(c)
print('a is c?', a is c)
print('a is b?', a is b, '\n')

# False Values:
#	1. False
#	2. None
#	3. Zero of any numeric type
#	4. Any empty sequence, e.g., '', (), [].
#	5. Any empty mapping, e.g., {}

condition = [False, None, 0, 10, '', 'Test', (), [], {}]

for cond in condition:

	if cond:
		print('"', cond, '" : evaluated to True\n')
	else:
		print('"', cond, '": evaluated to False\n')
