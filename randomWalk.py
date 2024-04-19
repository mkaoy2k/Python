"""This is an example of solving 'random-walk' problem. I.e.
What is the longest random walk you can take so that
on average you will end up 4 blocks or fewer from home
and no taxi needed."""
import random


def random_walk(n):
    """Return coordinates (a Tuple) after 'n'-block random walk."""
    x, y = 0, 0

    for i in range(n):
        step = random.choice(['E', 'W', 'S', 'N'])
        if step == 'E':
            x += 1
        elif step == 'W':
            x -= 1
        elif step == 'S':
            y -= 1
        else:
            y += 1
    return (x, y)


def random_walk_v2(n):
    """Return coordinates (a Tuple) after 'n'-block random walk."""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


if __name__ == '__main__':
    print(f'Random walk...')
    for i in range(25):
        walk = random_walk(10)
        print(f'{walk} \n\tDistance from home = {abs(walk[0]) + abs(walk[1])}')

    print(f'\nRandom walk v2...')
    for i in range(25):
        walk = random_walk_v2(10)
        print(f'{walk} \n\tDistance from home = {abs(walk[0]) + abs(walk[1])}')

    number_of_walks = 10_000
    blocks_limit = 5
    for walk_len in range(1, 36):
        no_taxi = 0  # <= 4 blocks from home
        for i in range(number_of_walks):
            (x, y) = random_walk_v2(walk_len)
            distance = abs(x) + abs(y)
            if distance <= blocks_limit:
                no_taxi += 1
        no_taxi_ratio = float(no_taxi) / number_of_walks * 100
        print(f'walk length: {walk_len}\n\tNo taxi ratio: {no_taxi_ratio}')

"""Last observation about the result: 31 or 33
Q: Why any even walk length has lower chance to walk home no taxi needed
than 2 adjacent odd walk lengths?"""
