import prompt
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


def congratulations(name):
    print(settings.CONGRATS.format(name))


def greetings():
    print(settings.GREETINGS)


def set_task(task):
    return get_answer(task['question'])
