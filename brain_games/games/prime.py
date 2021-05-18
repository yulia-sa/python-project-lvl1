#!/usr/bin/env python
from random import randint


GAME_QUESTION = (
    "Answer \"yes\" if given number is prime. "
    "Otherwise answer \"no\"."
)

NUMBERS_LEFT_BOUNDARY = 0
NUMBERS_RIGHT_BOUNDARY = 200


def is_prime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
        i += 1
    return True


def generate_game_data():
    random_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    answer = "yes" if is_prime(random_number) else "no"

    return str(random_number), answer
