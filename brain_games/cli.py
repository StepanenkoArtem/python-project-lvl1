import prompt


def show_message(message):
    print(message)


def ask_user_name():
    return prompt.string("May I have your name?: ")


def set_responce(response):
    print(response)


def user_answer(question):
    print("Question: {}".format(question))
    return prompt.string("Your answer:")
