# Function Examples
# 

# Positional parameters must come before keyword parameters
def hello_func(greeting, name = 'You'):
	return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name='Michael'))

def student_info(*args, **kwargs):
	print('\nStudent info listed below:')
	print('   ', args)
	print('   ', kwargs)

# Notice that "=" b/t keyword and value
# but return  ":" in a dictionary
student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

# Number of days per month, First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]

def is_leap(year):
	""" Return True for leap years,
	False for non-leap year."""

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	"""Return number of days, given a year and a month."""

	if not 1 <= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print('Year 2017 leap?', is_leap(2017))
print('2017/2 has:', days_in_month(2017, 2), 'days\n')

print('Year 2000 leap?', is_leap(2000))
print('2000/2 has:', days_in_month(2000, 2), 'days\n')

print('Year 2200 leap?', is_leap(2200))
print('2200/2 has:', days_in_month(2200, 2), 'days\n')

