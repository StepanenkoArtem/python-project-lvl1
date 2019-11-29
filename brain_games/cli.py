import prompt
from brain_games.settings import CORRECT, INCORRECT
import brain_games.settings as settings


def show_message(message):
    print(message)


def ask_user_name():
    return prompt.string("May I have your name?: ")


def set_responce(response):
    print(response)


def get_answer(question):
    print("Question: {}".format(question))
    return prompt.string("Your answer:")


def congratulations():
    print(settings.CONGRATS.format(user_name))


def greetings():
    print(settings.GREETINGS)


def set_task(task):
    user_answer = get_answer(task['question'])
    if user_answer == str(task['answer']):
        set_responce(CORRECT)
        return True
    else:
        set_responce(INCORRECT.format(user_answer,
                                      task['answer'], user_name))
        return False


greetings()
user_name = ask_user_name()
