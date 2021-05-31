#!/usr/bin/env python
import prompt

NUMBER_OF_ROUNDS = 3


def play(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game.GAME_QUESTION)

    i = 0
    while i < NUMBER_OF_ROUNDS:
        question_data, right_answer = game.generate_game_data()
        print("Question: " + question_data)
        user_answer = input("Your answer: ")
        if not user_answer.lower() == right_answer:
            message = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'.\n"
                f"Let's try again, {user_name}!"
            )
            print(message)
            return
        print("Correct!")
        i += 1

    print(f"Congratulations, {user_name}!")
    return
