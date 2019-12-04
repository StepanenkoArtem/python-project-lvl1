from settings import MAX, MIN
import random

TITLE = "Find the greatest common divisor of given numbers."


def calculate_gcd(a, b):
    if a > b:
        return calculate_gcd(a - b, b)
    elif b > a:
        return calculate_gcd(a, b - a)
    else:
        return a


def task():
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    question = '{} and {}'.format(a, b)
    answer = str(calculate_gcd(a, b))
    return question, answer
