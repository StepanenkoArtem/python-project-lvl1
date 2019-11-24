import prompt
from brain_games.even_settings import CORRECT, INCORRECT


def show_message(message):
    print(message)


def ask_user_name():
    return prompt.string("May I have your name?: ")


def set_responce(user_answer, correct_answer, user_name):
    if user_answer == correct_answer:
        print(CORRECT)
    else:
        print(INCORRECT.format(user_answer, correct_answer, user_name))


def get_answer(question):
    print("Question: {}".format(question))
    return prompt.string("Your answer:")

