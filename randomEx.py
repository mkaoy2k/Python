"""Examples of using random generator 'random' module
"""
import random
import math

from inspect import getmembers, ismethod

# Display methods in 'random' module, using "inspect" module
print(f'Display methods in "random" module')
for (name, member) in getmembers(random, ismethod):
    if not name.startswith("_"):
        print(f'===>{name}')


def draw_poker(n):
    '''Randomly draw n cards from a poker deck'''

    deck = list(range(0, 52))
    # card 0-51
    # 0 1 2 3 4 5 6 7 8 9 10 11 12
    # K A 2 3 4 5 6 7 8 9 10  J  Q
    deckCol = ['K', '1', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q']
    suits = ['Spade', 'Heart', 'Dimond', 'Club']
    hand = random.sample(deck, k=5)
    print('Select 5 cards from a Poker deck:\t', hand)

    kind = [math.floor(hand[i] / 13) for i in range(5)]

    color = [suits[kind[i]] for i in range(5)]
    point = [hand[i] % 13 for i in range(5)]
    point2 = [deckCol[point[i]] for i in range(5)]

    for i in range(n):
        print(color[i], point2[i])
    # print(point)
    print()


def gen_employee(n):
    """Another example using various random methods"""
    first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael',
                   'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

    last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson',
                  'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

    street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park',
                    'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

    fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield',
                   'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
              'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

    for num in range(n):
        first = random.choice(first_names)
        last = random.choice(last_names)

        phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

        street_num = random.randint(1, 999)
        street = random.choice(street_names)
        city = random.choice(fake_cities)
        state = random.choice(states)
        zip_code = random.randint(10000, 99999)
        address = f'{street_num} {street} St., {city}, {state} {zip_code}'

        email = first.lower() + last.lower() + '@bogusemail.com'
        salary = random.uniform(50, 150)
        print(
            f'===>{first} {last}\n{phone}\n{address}\n{email}\nSalary: ${salary:6.3f}K\n')


if __name__ == '__main__':

    draw_poker(5)
    gen_employee(5)
