from brain_games.even_settings import *
import brain_games.cli as cli
import random


def get_random_number():
    return random.randint(*RANGE)


def is_even(number):
    return not bool(number % 2)


def run():
    correct_answers = 0
    cli.greeting()
    print(GAME_TASK)
    player_name = cli.ask_name()
    while correct_answers < MIN_CORRECT_ANSWERS:
        random_number = get_random_number()
        if cli.get_answer(random_number) == is_even(random_number):
            cli.correct()
            correct_answers += 1
        else:
            cli.incorrect()
            exit()

    cli.congratulations(player_name)
