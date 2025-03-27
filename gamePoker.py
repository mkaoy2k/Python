"""Module for simulating a poker game with card drawing functionality.

This module provides a function to draw poker cards from a standard deck.
"""

import itertools
import random

def draw_poker(n):
    """Simulate drawing n cards from a standard poker deck.
    
    Args:
        n (int): Number of cards to draw
        
    Returns:
        list: A list of tuples representing the drawn cards
    """
    # Create the ranks for the deck (2-10, J, Q, K, A)
    ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
    ranks = [str(rank) for rank in ranks]  # Convert all ranks to strings

    # Create the suits for the deck
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    
    # Create the full deck by combining suits and ranks
    # Each card is represented as a tuple (suit, rank)
    deck = [card for card in itertools.product(suits, ranks)]

    # Generate all possible combinations of n cards from the deck
    # Each combination is a tuple of n cards
    hands = [hand for hand in itertools.combinations(deck, n)]

    # Print the number of possible combinations
    print(f'The number of {n}-card poker has {len(hands):,} combinations.')

    # Shuffle the hands and return one random hand
    draw = random.choice(hands)
    print(f'First {n}-card draw:\n{sorted(draw)}')
    return f'Your {n}-card draw:\n{sorted(draw)}'


if __name__ == '__main__':
    draw_poker(5)
