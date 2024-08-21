#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins: list, total: int) -> int:
    """ Given a pile of coins of different values
    determine the fewest number of coins needed to
    meet a given amount total"""
    coins.sort()
    counter = {key: 0 for key in coins}
    current_sum = 0
    remain = 0
    if total <= 0:
        return 0

    for i in range(len(coins) - 1, -1, -1):
        if coins[i] > total:
            continue

        if coins[i] == total:
            current_sum += coins[i]
            counter[coins[i]] += 1
            return sum([count for count in counter.values()])

        elif coins[i] < total and (current_sum + coins[i]) < total:
            current_sum += coins[i]
            counter[coins[i]] += 1
            remain = total - current_sum
            while ((remain - coins[i]) > 0 and
                   (current_sum + coins[i]) < total):
                current_sum += coins[i]
                counter[coins[i]] += 1
                remain = total - current_sum
            if remain in coins:
                current_sum += remain
                counter[coins[i]] += 1
                return sum([count for count in counter.values()])
            elif remain % coins[i] == 0:
                while (current_sum != total):
                    current_sum += coins[i]
                    counter[coins[i]] += 1
                return sum([count for count in counter.values()])
            else:
                continue

    return -1
