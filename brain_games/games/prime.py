from brain_games.settings import MIN, MAX
import random
import math

TITLE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divide_remainders = []
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        divide_remainders.append(number % i)
        if (0 in divide_remainders) or (number == 1):
            return False
    return True


def task():
    random_number = random.randint(MIN, MAX)
    question = str(random_number)
    true_answer = 'yes' if is_prime(random_number) else 'no'
    return question, true_answer
