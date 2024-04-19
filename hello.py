greeting = 'Hello'
name = 'Michael'

print('Concatenating strings with plus sign...')
message = greeting + ', ' + name + '. Welcome!'
print('===>', message)

print('Using a str-type "format" class method...')
message2 = '{}, {}. Welcome!'.format(greeting, name)
print('===>', message2)

print('Using f-formatter on Python 3, not available on Python 2...')
message3 = f'{greeting}, {name}. Welcome!'
print('===>', message3)

print('Converting a string to upper case...')
message4 = f'{greeting}, {name.upper()}. Welcome!'
print('===>', message4)

# find class methods and detail description of a method
print('Inquiring all class methods of a str-type variable "name":', name, '', dir(name))
print('Inquiring a class description, "str.lower()":')
help(str.lower)

