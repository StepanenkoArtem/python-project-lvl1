import brain_games.settings as settings
import brain_games.cli as cli
import random


TITLE = "What is the result of the expression?"


def summ(a, b):
    return {'question': '{} + {}'.format(a, b), 'answer': (a + b)}


def minus(a, b):
    return {'question': '{} - {}'.format(a, b), 'answer': (a - b)}


def mult(a, b):
    return {'question': '{} * {}'.format(a, b), 'answer': (a * b)}


def task():
    a = random.randint(*settings.RANGE)
    b = random.randint(*settings.RANGE)
    return random.choice([summ(a, b), minus(a, b), mult(a, b)])


def run():
    cli.show_message(TITLE)
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        if cli.set_task(task()):
            correct_answers += 1
        else:
            exit()
    cli.congratulations()
