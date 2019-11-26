from brain_games.settings import CORRECT, INCORRECT
import brain_games.settings as settings
import brain_games.cli as cli
import random


GAME_TASK = "What is the result of the expression?"


def summ(a, b):
    return {'question': '{} + {}'.format(a, b), 'answer': (a + b)}


def minus(a, b):
    return {'question': '{} - {}'.format(a, b), 'answer': (a - b)}


def mult(a, b):
    return {'question': '{} * {}'.format(a, b), 'answer': (a * b)}


def set_task():
    a = random.randint(*settings.RANGE)
    b = random.randint(*settings.RANGE)
    return random.choice([summ(a, b), minus(a, b), mult(a, b)])


def run():
    correct_answers = 0
    cli.show_message(settings.GREETINGS)
    print(GAME_TASK)
    user_name = cli.ask_user_name()
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        task = set_task()
        user_answer = int(cli.user_answer(task['question']))
        if user_answer == task['answer']:
            correct_answers += 1
            cli.set_responce(CORRECT)
        else:
            cli.set_responce(INCORRECT.format(user_answer,
                                              task['answer'], user_name))
            exit()

    cli.show_message(settings.CONGRATS.format(user_name))
