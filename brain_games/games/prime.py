import brain_games.cli as cli
import brain_games.settings as settings
import random
import math


TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_random_number():
    return random.randint(*settings.RANGE)


def is_prime(number):
    divide_remainders = []
    for i in range(2, math.floor(math.sqrt(number))+1):
        divide_remainders.append(number % i)
    if (0 in divide_remainders) or (number == 1):
        return 'no'
    else:
        return 'yes'


def task():
    random_number = get_random_number()
    return {"question": random_number, "answer": is_prime(random_number)}


def run():
    cli.show_message(TITLE)
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        if cli.set_task(task()):
            correct_answers += 1
        else:
            exit()
    cli.congratulations()
