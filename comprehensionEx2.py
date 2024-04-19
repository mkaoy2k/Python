"""More comprehension examples"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Number list {nums}\n')

# Populate a list for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print(f'Populate List in for-loop\n===>{my_list}\n')

# List comprehension to populate 'n' in nums
my_list2 = [n for n in nums]
print(f'List comprehension\n===>{my_list2}\n')

# Populate a list for each 'n*n' in nums
my_list = []
for n in nums:
  my_list.append(n * n)
print(f'Populate List in for-loop\n===>{my_list}\n')

# List comprehension to populate 'n*n' in nums
my_list2 = [n * n for n in nums]
print(f'List comprehension\n===>{my_list2}\n')

# Anonymous function lambda to populate 'n*n' in nums
# using map()
my_list3 = list(map(lambda n: n * n, nums))
print(f'lambda expression n*n \n===>{my_list3}\n')

# Populate a list for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
  if n % 2 == 0:
    my_list.append(n)

print(f'Populate List in for-loop even number \n===>{my_list}\n')

# List comprehension to populate 'n' in nums and if 'n' is even
my_list2 = [n for n in nums if n % 2 == 0]
print(f'List comprehension even number \n===>{my_list2}\n')

# Using annonymous function lambda() to populate 'n' in nums if 'n' is even
# with filter()
my_list3 = list(filter(lambda n: n % 2 == 0, nums))
print(f'lambda expression even number \n===>{my_list3}\n')

# Populate a list for each (letter, num) pair
# in 'abcd' and in '0123'
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter, num))
print(f'Populate List in for-loop letter-digit \n===>{my_list}\n')

# List comprehension to populate a list for each (letter, num) tuple
# in 'abcd' and in '0123'
my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
print(f'List comprehension letter-digit \n===>{my_list2}\n')

# Dictionary Comprehensions Example
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# The zip() function matches in pair
print(zip(names, heros))

my_dict = {}
for name, hero in zip(names, heros):
  my_dict[name] = hero
print(f'Populate Dict in for-loop actors \n===>{my_dict}\n')

# Dictionary comprehession to populate dict{'name': 'hero'}
# for each (name,hero) pair using zip()
my_dict2 = {name: hero for name, hero in zip(names, heros)}
print(f'Dict Comprehension actors \n===>{my_dict2}\n')

# If name not equal to Peter
my_dict3 = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(f'Dict Comprehension without name="Peter" \n===>{my_dict3}\n')

# Set Comprehension Example
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
print(f'With duplicated numbers {nums}')

# Populate a set for each 'n*n' in nums, eliminating duplicates
my_set = set()
for n in nums:
  my_set.add(n * n)
print(f'Populate Set in for-loop n*n \n===>{my_set}\n')

# All comprehension styles
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'All comprehension styles: {nums}\n')

# Set Comprehension to populate 'n' in nums
my_set2 = {n * n for n in nums}
print(f'Set comprehension n*n \n===>{my_set2}\n')

# Tuple comprehension to populate 'n*n' in nums
my_tuple = (n * n for n in nums)
print(f'Tuple comprehension n*n \n===>{tuple(my_tuple)}')
print(f'tuple comprehension is type of {type(my_tuple)}\n')

# List comprehesion to populate 'n*n' in nums
my_list = [n * n for n in nums]
print(f'List comprehension n*n \n===>{my_list}\n')
# Generator Expression to yield 'n*n' in nums


def gen_func(nums):
  for n in nums:
    yield n * n


my_gen = gen_func(nums)
print(f'Generator expression n*n\n===>', end="")
for i in my_gen:
  print(i, end=" ")
print()
