#!/usr/bin/env python
import prompt

ROUNDS_NUMBER = 3


def play(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game.GAME_RULES)

    i = 0
    while i < ROUNDS_NUMBER:
        question_data, right_answer = game.generate_game_data()
        print("Question: " + str(question_data))
        user_answer = input("Your answer: ")
        if not user_answer.lower() == str(right_answer):
            print(f"'{user_answer.lower()}' is wrong answer ;(. \
                    Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print("Correct!")
        i += 1

    print(f"Congratulations, {user_name}!")
    return
