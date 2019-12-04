import cli
from settings import MIN_CORRECT_ANSWERS
from messages import CORRECT, INCORRECT, GREETINGS, CONGRATS


def run(generate_round):
    cli.show_message(GREETINGS)
    user_name = cli.ask_user_name()
    cli.show_message(generate_round.TITLE)
    right_answers = 0
    while right_answers < MIN_CORRECT_ANSWERS:
        question, true_answer = generate_round.task()
        user_answer = cli.get_answer(question)
        if user_answer != true_answer:
            cli.show_message(
                INCORRECT.format(
                    user_answer,
                    true_answer,
                    user_name))
            break
        else:
            right_answers += 1
            cli.show_message(CORRECT)
            if right_answers == MIN_CORRECT_ANSWERS:
                cli.show_message(CONGRATS.format(user_name))
