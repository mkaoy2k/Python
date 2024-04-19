import itertools
import random

def draw_poker (n):
    """Poker Game: Five card draw"""

    # make a deck of cards iterable?
    ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
    ranks = [str(rank) for rank in ranks]

    # print(f'Ranks: {ranks}')

    suits = ["Spades", "Hearts", "Dimonds", "Clubs"]
    deck = [card for card in itertools.product(suits, ranks)]

    # for (index, card) in enumerate(deck):
    #     print(f'{1+index}: {card}')

    hands = [hand for hand in itertools.combinations(deck, n)]
    print(f'The number of 5-card poker has {len(hands):,} combinations.')

    # randomly pick 5 unique cards in one draw, using choices() method
    draw = list(random.choices(deck, k=n))
    print(f'First 5-card draw:\n{sorted(draw)}')

    # alternatively, using sample() method
    draw = list(random.sample(deck, k=n))
    return f'Your {n}-card draw:\n{sorted(draw)}'


if __name__ == '__main__':
    draw_poker(5)
