#!/usr/bin/env python
from random import randint


GAME_QUESTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10

PROGRESSION_START_LEFT_BOUNDARY = 0
PROGRESSION_START_RIGHT_BOUNDARY = 100

PROGRESSION_STEP_LEFT_BOUNDARY = 1
PROGRESSION_STEP_RIGHT_BOUNDARY = 10


def create_progression(start, step, length):
    progression = [
        start + (i * step)
        for i in range(1, length + 1)
    ]

    return progression


def generate_game_data():
    progression_start = randint(PROGRESSION_START_LEFT_BOUNDARY,
                                PROGRESSION_START_RIGHT_BOUNDARY)
    progression_step = randint(PROGRESSION_STEP_LEFT_BOUNDARY,
                               PROGRESSION_STEP_RIGHT_BOUNDARY)

    progression = create_progression(progression_start,
                                     progression_step,
                                     PROGRESSION_LENGTH)

    guess_number_index = randint(0, len(progression) - 1)
    guess_number = progression[guess_number_index]
    progression[guess_number_index] = ".."

    return " ".join(map(str, progression)), str(guess_number)
