# loopEx
#

nums = [1, 2,3 ,4, 5]
print('The number list:', nums)
print('   looping each item...')

for num in nums:
	print('   ', num)

# break and continue in loop
#
print('\n   Breaking out of a for loop...')
for num in nums:
	if num == 3:
		print('   ', num, 'Found!')
		break
	print('   ', num)

print('\n   Continuing within a for loop...')
for num in nums:
	if num == 3:
		print('   ', num, 'Found!')
		continue
	print('   ', num)

# nested for loops
#
print('\n   two nested loops...')
for num in nums:
	for letter in 'abc':
		print('   ', num, letter)

print('\nfor-loop ranging from 0 to 9...')
for i in range(10):
	print('   ', i)

print('\nfor-loop ranging from 1 to 10...')
for i in range(1, 11):
	print('   ', i)

print('\nwhile-loop ranging from 0 to 9...')
x = 0
while x < 10:
	print('   ', x)
	x += 1

