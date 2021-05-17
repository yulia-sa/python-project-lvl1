#!/usr/bin/env python
from random import randint


GAME_QUESTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."

NUMBERS_LEFT_BOUNDARY = 0
NUMBERS_RIGHT_BOUNDARY = 100


def is_even(number):
    return "yes" if number % 2 == 0 else "no"


def generate_game_data():
    random_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    answer = is_even(random_number)
    return str(random_number), answer
