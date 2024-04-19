class Martian:
    """Someone who lives on Mars."""

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        print(f"===> You set {name} = {value}")
        self.__dict__[name] = value

    def __getattr__(self, name):
        print(f"===> Get the '{name}' attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No attribute name '{name}' found")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __lt__(self, other):
        print(f"===> Comparing {self} with {other}")
        if self.last_name != other.last_name:
            return (self.last_name < other.last_name)
        else:
            return (self.first_name < other.first_name)


# Print "__doc__" Attribute where doc-string is stored
print(f'Printing __doc__:\n===>{Martian.__doc__}\n')

# Print "__dict__" Attribute where class attributes are stored
m1 = Martian('Michael', 'Kao')
m1.arrival_date = '2035-12-22'
print(f'Printing __dict__:\n===>{m1.__dict__}\n')

# Get attributes. Note: __getattr__() not invoked
print(f'First name = {m1.first_name}')
print(f'Last name = {m1.last_name}')

# __getattr__() used for computed attributes
print(m1.full_name)

try:
    print(m1.martian_name)
except:
    print(f"===> AttributeError caught\n")

# computed attributes are not stored in __dict__
print(f'Printing __dict__:\n===>{m1.__dict__}\n')

# # Print obj address
# print(f'Obj instance address in hex:\n===>{m1}\n')
# print(f'Obj __str__() method in hex:\n===>{m1.__str__()}\n')
# print(f'Obj instance address in hex:\n===>{id(m1)}\n')
#
# overwrite_str = """Trying to overwrite __str__() method by:
# def __str__(self):
#     return f"{self.first_name} {self.last_name}"
#
# ===>To change the default behavior
# """
# print(overwrite_str)

# comparing two martians by name
m2 = Martian("Henry", "Kao")
m3 = Martian("Christine", "Kao")
m4 = Martian("Judy", "Kao")
m5 = Martian("Latte", "Dog")
m6 = Martian("Olisan", "Dog")

martians = [m1, m2, m3, m4, m5, m6]
martians.sort()
for m in martians:
    print(f"===>{m}")
