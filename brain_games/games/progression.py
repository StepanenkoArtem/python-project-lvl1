import brain_games.settings as settings
import brain_games.cli as cli
import random


TITLE = "What number is missing in the progression?"


def create_progression(start, step):
    progress = []
    while len(progress) < settings.PROGR_LENGTH:
        progress.append(start)
        start = start + step
    return progress


def task():
    start = random.randint(*settings.RANGE)
    step = random.randint(*settings.RANGE)
    progression_list = create_progression(start, step)
    excluded_index = random.randint(0, (len(progression_list)-1))
    excluded_item = progression_list.pop(excluded_index)
    progression_list.insert(excluded_index, " ")
    return {'question': progression_list, 'answer': excluded_item}


def run():
    cli.show_message(TITLE)
    correct_answers = 0
    while correct_answers < settings.MIN_CORRECT_ANSWERS:
        if cli.set_task(task()):
            correct_answers += 1
        else:
            exit()
    cli.congratulations()
