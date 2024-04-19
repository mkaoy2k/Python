"""Example: make a deck of Poker cards iterable
一付樸克牌52張中抽5張有幾種可能組合"""

import itertools
import glog as log

log.setLevel("INFO")
# log.setLevel("DEBUG")

log.info(f'首先建立一付牌...')

# 從小到大排序 2, 3, 4, 5,6, 7, 8, 9, 10, J, Q, K, A
ranks = list(range(2, 11)) + ["J", "Q", "K", "A"]
ranks = [str(rank) for rank in ranks]
log.info(f'從小到大排序:\n===>{ranks}')

# 四花色
suits = ["黑桃", "紅心", "紅鑽", "黑梅"]
log.info(f'四花色:\n===>{suits}')

# 一付牌放成列表
deck = [card for card in itertools.product(suits, ranks)]

log.info(f'一付樸克牌有..')
for (index, card) in enumerate(deck):
    log.debug(f'{1+index}: {card}')
log.info(f'===> 共 {len(deck)} 張')

hands = [hand for hand in itertools.combinations(deck, 5)]
for hand in hands:
    log.debug(hand)
log.info(f'===> 一付樸克牌52張中抽5張有 {len(hands):,} 可能組合.')
