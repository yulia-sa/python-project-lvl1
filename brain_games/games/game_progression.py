#!/usr/bin/env python
from random import randint


GAME_QUESTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10

PROGRESSION_START_LEFT_BOUNDARY = 0
PROGRESSION_START_RIGHT_BOUNDARY = 100

PROGRESSION_STEP_LEFT_BOUNDARY = 1
PROGRESSION_STEP_RIGHT_BOUNDARY = 10


def generate_game_data():
    progression_start = randint(PROGRESSION_START_LEFT_BOUNDARY,
                                PROGRESSION_START_RIGHT_BOUNDARY)
    progression_step = randint(PROGRESSION_STEP_LEFT_BOUNDARY,
                               PROGRESSION_STEP_RIGHT_BOUNDARY)

    progression = [progression_start]
    for i in range(PROGRESSION_LENGTH - 1):
        progression_last_number = progression[-1]
        progression.append(progression_last_number + progression_step)

        guess_number_index = randint(0, PROGRESSION_LENGTH - 1)

    guess_number = progression[guess_number_index]
    progression[guess_number_index] = ".."

    return " ".join(map(str, progression)), guess_number
