#!/usr/bin/env python
from random import randint, choice

GAME_RULES = "What is the result of the expression?"

NUMBERS_LEFT_BOUNDARY = 0
NUMBERS_RIGHT_BOUNDARY = 10


def generate_game_data():
    first_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    second_number = randint(NUMBERS_LEFT_BOUNDARY, NUMBERS_RIGHT_BOUNDARY)
    operator = choice(["+", "-", "*"])

    if operator == "+":
        answer = first_number + second_number
    elif operator == "-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number

    return (f"{first_number} {operator} {second_number}"), answer
