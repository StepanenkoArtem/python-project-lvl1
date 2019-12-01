import brain_games.settings as settings
import random


TITLE = "What is the result of the expression?"


def summ(a, b):
    return {'question': '{} + {}'.format(a, b), 'answer': (a + b)}


def minus(a, b):
    return {'question': '{} - {}'.format(a, b), 'answer': (a - b)}


def mult(a, b):
    return {'question': '{} * {}'.format(a, b), 'answer': (a * b)}


def calc():
    a = random.randint(*settings.RANGE)
    b = random.randint(*settings.RANGE)
    return random.choice([summ(a, b), minus(a, b), mult(a, b)])
