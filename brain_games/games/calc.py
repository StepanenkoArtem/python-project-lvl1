from settings import MIN, MAX
import random


TITLE = "What is the result of the expression?"


def task():
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    variants = [('{} + {}'.format(a, b), a + b),
                ('{} - {}'.format(a, b), a - b),
                ('{} * {}'.format(a, b), a * b)]
    question, true_answer = random.choice(variants)
    return question, str(true_answer)
