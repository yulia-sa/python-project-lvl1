#!/usr/bin/env python
from random import randint


GAME_RULES = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."

NUMBERS_LEFT_BOUNDARY = 0
NUMBERS_RIGHT_BOUNDARY = 200


def generate_game_data():
    random_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    for i in range (2, random_number // 2):
        if random_number % i == 0:
            return random_number, "no"
        i += 1
    return random_number, "yes"
