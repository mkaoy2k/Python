# Advanced formatting Examples
#

person = {'name': 'Jenn', 'age': 23}
print('Formating A Dictionary:\t', person)

sentence = 'My name is ' + person['name'] + \
    ' and I am ' + str(person['age']) + ' years old.'
print('\tBy concadnating strings:\t', sentence)


sentence = 'My name is {} and I am {} years old.'.format(
    person['name'], person['age'])
print('\tBy format function:\t', sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(
    person['name'], person['age'])
print('\tBy positional 0-indexed:\t', sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(
    person['name'], person['age'])
print('\tAccessing key in parms:\t', sentence)

sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(
    person, person)
print('\tAccessing key in format place-holders:\t', sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print('\tPassing Single parm of dictionary:\t', sentence)

li = ['Jenn', 23]
print('Formating a list:\t', li)
sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(li)
print('\tAccessing list by index:\t', sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', '33')
print('Formating an object:\t', p1)

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print('\tAccessing attr:\t', sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(
    name='Jenn', age='30')
print('\tSubstituting with parms:\t', sentence)

sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print('\tMost recommended way for readability:\t', sentence)

for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

print('Formating padding digits:\t')
for i in range(1, 11):
    sentence = '\tThe padded value is {:03}'.format(i)
    print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to:\t {}'.format(pi)
print(sentence)
print('Formating after decimal point:\t')

sentence = '\tPi is truncated to:\t {:0.3f}'.format(pi)
print(sentence)


sentence = '1 MB is equal to {} bytes'.format(1000**2)
print(sentence)
print('Formating a number by commas and decimals:\t')
sentence = '1 MB is equal to {:,.02f} bytes'.format(1000**2)
print('\t', sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print('Formating a date:\t')
print('\t', my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print('\t', sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
    my_date)

print(sentence)
