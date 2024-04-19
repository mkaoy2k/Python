# Duck Typing and Easier to ask forgiveness than permission (EAFP)

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):

    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Look before you leap, Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # Pythonic
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


print('Duck typed Pythonic example:')
d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


# Easier to ask forgiveness than permission (EAFP)
# Advantages:
# 1. readability
# 2. reducing multiple access to object
# 3. avoiding racing condition

# reducing multiple access
my_list = [1, 2, 3, 4, 5]


# Non-Pythonic
print('\nNon-Pythonic List example:')
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('That index does not exist')

# Pythonic
print('\nPythonic List example:')

try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')

# racing-condition example
import os

my_file = "/tmp/teest.txt"

# Race Condition
print('\nNon-Pythonic Race-Condition example:')
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can not be accessed')

# No Race-Condition
print('\nPythonic Race-Condition example:')
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())
