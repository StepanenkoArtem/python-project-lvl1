from settings import MIN, MAX
import random


TITLE = 'Answer "yes" if number even otherwise answer "no"'


def task():
    question = random.randint(MIN, MAX)
    answer = 'no' if question % 2 else 'yes'
    return question, answer
