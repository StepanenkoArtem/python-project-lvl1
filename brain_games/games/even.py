import brain_games.settings as settings
import random

# Subtitle
TITLE = 'Answer "yes" if number even otherwise answer "no"'


def get_random_number():
    return random.randint(*settings.RANGE)


def is_even(number):
    return 'yes' if not (number % 2) else 'no'


def even():
    random_integer = get_random_number()
    return {"question": random_integer, "answer": is_even(random_integer)}
