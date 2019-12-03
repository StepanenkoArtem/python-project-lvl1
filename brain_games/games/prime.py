from brain_games import settings
import random
import math

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_random_number():
    return random.randint(*settings.RANGE)


def is_prime(number):
    divide_remainders = []
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        divide_remainders.append(number % i)
    if (0 in divide_remainders) or (number == 1):
        return 'no'
    else:
        return 'yes'


def task():
    random_number = get_random_number()
    question = str(random_number)
    true_answer = is_prime(random_number)
    return question, true_answer
