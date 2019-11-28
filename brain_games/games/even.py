from brain_games.settings import CORRECT, INCORRECT
import brain_games.settings as settings
import brain_games.cli as cli
import random

# Subtitle
GAME_TASK = 'Answer "yes" if number even otherwise answer "no"'


def get_random_number():
    return random.randint(*settings.RANGE)


def is_even(number):
    return 'yes' if not (number % 2) else 'no'


def task():
    random_integer = get_random_number()
    return {"question": random_integer, "answer": is_even(random_integer)}


def run():
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        if cli.set_task(task()):
            correct_answers += 1
        else:
            exit()
    cli.congratulations()