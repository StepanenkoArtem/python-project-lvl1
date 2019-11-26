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


def run():
    correct_answers = 0
    cli.show_message(settings.GREETINGS)
    cli.show_message(GAME_TASK)
    user_name = cli.ask_user_name()
    cli.show_message('Hello, {}'.format(user_name))
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        random_number = get_random_number()
        user_answer = cli.user_answer(random_number).lower()
        if user_answer == is_even(random_number):
            correct_answers += 1
            cli.set_responce(CORRECT)
        else:
            cli.set_responce(
                INCORRECT.format(user_answer, is_even(random_number), user_name)
            )
            exit()

    cli.show_message(settings.CONGRATS.format(user_name))
