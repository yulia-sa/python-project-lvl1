#!/usr/bin/env python
from random import randint


GAME_QUESTION = "Find the greatest common divisor of given numbers."

NUMBERS_LEFT_BOUNDARY = 1
NUMBERS_RIGHT_BOUNDARY = 50


def find_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

    gcd = first_number + second_number

    return gcd


def generate_game_data():
    first_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    second_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)

    answer = find_gcd(first_number, second_number)

    return f"{first_number} {second_number}", str(answer)
