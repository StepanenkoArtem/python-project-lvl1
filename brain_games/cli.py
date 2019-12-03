import prompt


def show_message(message):
    print(message)


def ask_user_name():
    return prompt.string("May I have your name?: ")


def get_answer(question):
    print("Question: {}".format(question))
    return str(prompt.string("Your answer:"))


def set_task(task):
    return get_answer(task['question'])
