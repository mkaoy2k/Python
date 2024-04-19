"""A regular expression, or regex, is a pattern that can be used to match
and manipulate strings in Python.

The re module in Python provides a set of functions for
working with regular expressions.
"""
import re
from inspect import getmembers, isclass, isfunction

#  Display classes in 're' module
print(f'Display classes in "re" module')
for (name, member) in getmembers(re, isclass):
    if not name.startswith("_"):
        print(f'===>{name}')
print()

# Display functions in 're' module
print(f'Display functions in "re" module')
for (name, member) in getmembers(re, isfunction):
    if not name.startswith("_"):
        print(f'===>{name}')
print()

# Example of matching patterns in a string
print(f"Example of matching patterns in a string...")

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
print(f"==>{text_to_search}<==")

# match 800- and 900-phone numbers
pattern0 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# match phone numbers
pattern1 = re.compile(r'\d{3}.\d{3}.\d{4}')

# match Mr....
pattern2 = re.compile(r'Mr\.? [A-Z]\w*')

# match all Mr. Ms. and Mrs...
pattern3 = re.compile(r'(Mr|Ms|Mrs)\.? [A-Z]\w*')

matches = pattern3.finditer(text_to_search)

# print(matches)
for match in matches:
    print(f"===>{match}")
print()

# Example of matching a pattern (case-ignored) from a sentence
print(f"Example of matching a pattern (case-ignored) from a sentence...")

sentence = 'Start a sentence and then bring it to an end'
print(f"==>{sentence}<==")

pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(f"===>{matches}")
print()

print("Example of re-usable compiled pattern...")

urls = '''https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
print(f"==>{urls}<==\n")

"""
The re.compile() function is used to precompile a regular expression
pattern, creating a regular expression object that can be used for
pattern matching. This can be useful in situations where the same
regular expression will be used multiple times, as it allows the
pattern to be compiled once, and then used repeatedly,
rather than having to recompile the pattern each time it is used.

Additionally, compile() can take some optional parameters like
re.IGNORECASE,
re.DOTALL,
re.MULTILINE and so on, that allow you to define how
the regular expression should behave.
"""

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Using compiled Pattern to find the 2nd & 3rd parts of urls
subbed_urls = pattern.sub(r'\2\3', urls)

# Example of filtering 'www' out of URL's
print("Filtering 'www' out of URL list...")
print(f'===>subbed_url is {type(subbed_urls)}\n===>{subbed_urls}<==')

# Using compiled Pattern to find the 3rd group
print("Printing the 3rd group of matched strings...")
matches = pattern.finditer(urls)

for match in matches:
    str = match.group(3)
    print(f'===>{str}')

# Example of matching pattern from a file
# with open('person_data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)
