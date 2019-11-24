from brain_games.even_settings import RANGE, MIN_CORRECT_ANSWERS, GREETINGS, CONGRATS
import brain_games.cli as cli
import random

# Subtitle
GAME_TASK = 'Answer "yes" if number even otherwise answer "no"'


def get_random_number():
    return random.randint(*RANGE)


def is_even(number):
    return 'yes' if not (number % 2) else 'no'


def run():
    correct_answers = 0
    cli.show_message(GREETINGS)
    cli.show_message(GAME_TASK)
    user_name = cli.ask_user_name()
    cli.show_message('Hello, {}'.format(user_name))
    while correct_answers < MIN_CORRECT_ANSWERS:
        random_number = get_random_number()
        user_answer = cli.get_answer(random_number).lower()
        cli.set_responce(user_answer, is_even(random_number), user_name)
        if user_answer == is_even(random_number):
            correct_answers += 1
        else:
            exit()

    cli.show_message(CONGRATS.format(user_name))
