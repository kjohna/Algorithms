#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

cache = {
    0: 1,
    1: 1,
    2: 2,
    3: 4
}


def eating_cookies(n, dump=None):
    ways = 0
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        if n not in cache:
            cache[n] = eating_cookies(n - 1) + \
                eating_cookies(n - 2) + \
                eating_cookies(n - 3)
        ways = cache[n]
    return ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
