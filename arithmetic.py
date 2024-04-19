# Arithmetic Operators:
#
# Addition:              
print('3 + 2 is...')
print('   ', 3 + 2)

# Subtraction:         
print('3 - 2 is...')
print('   ', 3 - 2)

# Multiplication:       
print('3 * 2 is...')
print('   ', 3 * 2)

# Division:
print('3 / 2 is...')               
print('   ', 3 / 2)

# Floor Division:      
print('3 // 2 is...')
print('   ', 3 // 2)

# Exponent:
print('3 ** 2 is...')             
print('   ', 3 ** 2)

# Modulus: 
print('3 % 2 is...')              
print('   ', 3 % 2)

# Test even or odd numbers with Modulus operator
m = 5
if (m % 2):
	print(m, 'is an odd nmuber!')
else :
	print(m, 'is an even number!')

# Built-in functions
#
# abs
m = -4
print(m, ' with the absolute value=', abs(m))

# round to the nearest integer
m = 3.45
n = 5.55
print(m, 'rounded to the nearest integer=', round(m))

# round to the first after decimal
print(m, 'rounded to the first after decimal=', round(m,1))
print(n, 'rounded to the first after decimal=', round(n,1))

# Comparisons:
#
# Equal: ==
num_1 = 3
num_2 = 2
print(num_1, ' == ', num_2, '?')
print ('   ', num_1 == num_2)

# Not Equal: !=
print(num_1, ' != ', num_2, '?')
print ('   ', num_1 != num_2)

# Greater Than: >
print(num_1, ' > ', num_2, '?')
print ('   ', num_1 > num_2)

# Less Than: <
print(num_1, ' < ', num_2, '?')
print ('   ', num_1 < num_2)

# Greater or Equal: >=
print(num_1, ' >= ', num_2, '?')
print ('   ', num_1 >= num_2)

# Less or Equal: <=
print(num_1, ' <= ', num_2, '?')
print ('   ', num_1 <= num_2)

# Type casting
#
num_1 = int('100')
print(num_1, ' is an integer, adding itself...')
print('   ', num_1 + num_1, 'is an integer!')

str_1 = str(num_1)
print(str_1, ' is a string, adding itself...')
print('   ', str_1 + str_1, 'is a string!')


