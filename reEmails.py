import re

emails = '''
ada@example.com
ada@university.edu
ada-321@my-work.net
'''
print(f'{emails}')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
print(f'{pattern}')
matches = pattern.finditer(emails)
for match in matches:
    print(f'==> {match}')
print()

emails = '''
ada@example.com
ada@university.edu
ada-321@my-work.net
'''
pattern = re.compile(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}')
print(f'{pattern}')
matches = pattern.finditer(emails)
for match in matches:
    print(f'==> {match}')
