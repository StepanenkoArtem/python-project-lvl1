import prompt


def greeting():
    print('Welcome to Brain Games!')


def ask_name():
    name = prompt.string("May I have your name?: ")
    print("Hello, {}\n".format(name))
    return name


def correct():
    print("Correct!")


def incorrect():
    print("'yes' is wrong answer ;(.Correct answer was 'no'.\n "
          "Let's try again, Bill!'")


def get_answer(number):
    print("Question: {}".format(number))
    answer = prompt.string("Is it even (yes/no):").lower()
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    else:
        return None


def congratulations(name):
    print("Great game, {}!".format(name))
