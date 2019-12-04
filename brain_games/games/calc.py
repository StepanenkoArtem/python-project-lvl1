from settings import MIN, MAX
import random
import operator


TITLE = "What is the result of the expression?"


def task():

    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    variants = [('{} + {}'.format(a, b), operator.add(a, b)),
                ('{} - {}'.format(a, b), operator.sub(a, b)),
                ('{} * {}'.format(a, b), operator.mul(a, b))]
    question, true_answer = random.choice(variants)
    return question, str(true_answer)
