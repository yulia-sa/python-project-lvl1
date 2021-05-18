#!/usr/bin/env python
from random import randint


GAME_QUESTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."

NUMBERS_LEFT_BOUNDARY = 0
NUMBERS_RIGHT_BOUNDARY = 100


def is_even(number):
    return True if number % 2 == 0 else False


def generate_game_data():
    random_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    answer = "yes" if is_even(random_number) else "no"

    return str(random_number), answer
