#!/usr/bin/env python
from brain_games.engine import play
from brain_games.games import game_gcd


def main():
    play(game_gcd)


if __name__ == '__main__':
    main()
