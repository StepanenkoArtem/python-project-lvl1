from brain_games.settings import PROGR_LENGTH, MIN, MAX
import random


TITLE = "What number is missing in the progression?"


def task():
    answer = ''
    question = []
    start = random.randint(MIN, MAX)
    step = random.randint(MIN, MAX)
    random_index = random.randint(0, PROGR_LENGTH-1)
    while len(question) < PROGR_LENGTH:
        question.append(start)
        if question.index(start) == random_index:
            answer = str(question.pop())
            question.append(' ')
        start = start + step
    return question, answer
