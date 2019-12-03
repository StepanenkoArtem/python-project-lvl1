import cli
import settings
from settings import CORRECT, INCORRECT


def run(generate_round):
    cli.greetings()
    user_name = cli.ask_user_name()
    right_answers = 0
    while right_answers < settings.MIN_CORRECT_ANSWERS:
        question, true_answer = generate_round.task()
        user_answer = cli.get_answer(question)
        if user_answer == true_answer:
            cli.set_responce(CORRECT)
            right_answers += 1
        else:
            cli.set_responce(
                INCORRECT.format(
                    user_answer,
                    true_answer,
                    user_name))
            exit()
    cli.congratulations(user_name)
