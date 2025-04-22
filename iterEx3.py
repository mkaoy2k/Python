"""
Example: make a deck of Poker cards iterable
一付樸克牌52張中抽5張有幾種可能組合
"""

import itertools
import logging

# 設定 logging 格式
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def create_deck():
    """
    建立一副完整的撲克牌
    Returns:
        list: 包含所有撲克牌的列表
    """
    # 從小到大排序 2, 3, 4, 5,6, 7, 8, 9, 10, J, Q, K, A
    ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
    ranks = [str(rank) for rank in ranks]
    logging.info(f'從小到大排序:\n===>{ranks}')

    # 四花色
    suits = ["黑桃", "紅心", "紅鑽", "黑梅"]
    logging.info(f'四花色:\n===>{suits}')

    # 一付牌放成列表
    deck = [card for card in itertools.product(suits, ranks)]
    return deck


def calculate_combinations(deck):
    """
    計算從一副牌中抽取5張的所有可能組合
    Args:
        deck (list): 撲克牌列表
    Returns:
        list: 所有可能的5張牌組合
    """
    hands = [hand for hand in itertools.combinations(deck, 5)]
    return hands


def main():
    """
    主函數，執行撲克牌組合計算
    """
    logging.info(f'首先建立一付牌...')
    
    # 建立一副牌
    deck = create_deck()
    logging.info(f'一付樸克牌有..')
    for (index, card) in enumerate(deck):
        logging.debug(f'{1+index}: {card}')
    logging.info(f'===> 共 {len(deck)} 張')

    # 計算所有可能的5張牌組合
    hands = calculate_combinations(deck)
    for hand in hands:
        logging.debug(hand)
    logging.info(f'===> 一付樸克牌52張中抽5張有 {len(hands):,} 可能組合.')


if __name__ == "__main__":
    main()
