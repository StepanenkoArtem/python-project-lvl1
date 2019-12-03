from settings import RANGE
import random

TITLE = "Find the greatest common divisor of given numbers."


def calculate_gcd(a, b):
    if a > b:
        return calculate_gcd(a - b, b)
    elif b > a:
        return calculate_gcd(a, b - a)
    else:
        return a


def gcd():
    a = random.randint(*RANGE)
    b = random.randint(*RANGE)
    return {
        'question': '{} and {}'.format(a, b),
        'answer': calculate_gcd(a, b)
    }
