#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    else:
        return rps_helper(rock_paper_scissors(n-1))


def rps_helper(games):
    moves = ['rock', 'paper', 'scissors']
    result = []
    for game in games:
        for move in moves:
            new_game = game[:]
            new_game.append(move)
            result.append(new_game)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
