#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """ Given a pile of coins of different values
    determine the fewest number of coins needed to
    meet a given amount total"""
    coins.sort()
    counter = {key: 0 for key in coins}
    current = 0
    remain = 0
    if total <= 0:
        return 0
    for i in range(len(coins) - 1, -1, -1):
        if coins[i] > total:
            continue

        elif coins[i] < total:
            current += coins[i]
            counter[coins[i]] += 1
            remain = total - current
            while ((remain - coins[i]) > 0):
                current += coins[i]
                counter[coins[i]] += 1
                remain = total - current
            if remain in coins:
                current += remain
                counter[coins[i]] += 1
                return sum([count for count in counter.values()])
            elif remain % coins[i] == 0:
                while (current != total):
                    current += coins[i]
                    counter[coins[i]] += 1
                return sum([count for count in counter.values()])
            else:
                continue
    return -1
