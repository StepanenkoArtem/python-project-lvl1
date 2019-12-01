import brain_games.cli as cli
import brain_games.settings as settings
from brain_games.settings import CORRECT, INCORRECT


def run(game, title):
    cli.greetings()
    user_name = cli.ask_user_name()
    cli.show_message(title)
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        task = game()
        user_answer = str(cli.get_answer(task['question']))
        if str(task['answer']) == user_answer:
            cli.set_responce(CORRECT)
            correct_answers += 1
        else:
            cli.set_responce(
                INCORRECT.format(
                    user_answer,
                    task['answer'],
                    user_name))
            exit()
    cli.congratulations(user_name)
