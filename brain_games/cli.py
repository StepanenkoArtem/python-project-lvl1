import prompt


def greeting():
    print('Welcome to Brain Games!')


def run():
    name = prompt.string("May I have your name?: ")
    print("Hello, {}".format(name))
