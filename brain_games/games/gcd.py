import brain_games.settings as settings
from brain_games.settings import RANGE
import brain_games.cli as cli
import random

TITLE = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    if a > b:
        return gcd(a - b, b)
    elif b > a:
        return gcd(a, b - a)
    else:
        return a


def task():
    a = random.randint(*RANGE)
    b = random.randint(*RANGE)
    return {'question': '{} and {}'.format(a, b), 'answer': gcd(a, b)}


def run():
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        if cli.set_task(task()):
            correct_answers += 1
        else:
            exit()
    cli.congratulations()
