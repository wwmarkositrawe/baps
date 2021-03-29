import random
import time
import os
import itertools
import threading
import sys
from threading import Timer
from alive_progress import alive_bar, config_handler, bouncing_spinner_factory

config_handler.set_global(length="35", bar="smooth",
                          force_tty=False, enrich_print=True)
hng_spinner = bouncing_spinner_factory('🛴', 10, hiding=False)
os.system('')  # allows to print ANSI codes in terminal

MAX_MAGIC_LEN = 10000
WORDS_SIMPLE = []
WORDS_AVANGARDE = []
PREFIXES = ['pane', 'mono', 'dyne', 'mini', 'mine', 'tele', 'poli', 'semi',
            'mane', 'tone', 'pine', 'solo', 'pupu', 'titi', 'mumu', 'pipi',
            'para', 'nima', 'mana', 'tera', 'tite', 'pima', 'piba', 'breś',
            'tra', 'pra', 'sra', 'fra', 'bra', 'mra', 'bry', 'pry', 'sry',
            'cim', 'pre', 'sraj', 'preś', 'miau', 'sple', 'sper']


def esc(code):
    return f'\033[{code}m'


def main():
    select_mode()


def select_mode():
    modeString = input(
        "\nHEJ HEJ. By chciałeś/lubiałeś w trybie podstawowym (0), czy dla cwaniaka (1) " +
        "w ramach tzw. trybu premp, powiedz szczerze: ")
    print()
    if modeString in ("w trybie podstawowym", "0"):
        create_word_basic(modeString)
        output_words(WORDS_SIMPLE)
    elif modeString in ("dla cwaniaka", "1", "premp"):
        create_word_avantgarde(modeString)
        output_words(WORDS_AVANGARDE)
    else:
        print(esc('31;1;4') + ("że co robi?") + esc(0) + ' cim oyunu \n')


def create_word_basic(modeString):
    for i in range(0, MAX_MAGIC_LEN):
        letters = []
        first_letter = random.choice("bpm")
        letters.append(first_letter)
        second_letter = random.choice("ia")
        letters.append(second_letter)
        third_letter = random.choice("bpm")
        letters.append(third_letter)
        fourth_letter = second_letter
        letters.append(fourth_letter)
        fifth_letter = random.choice("bp")
        letters.append(fifth_letter)
        sixth_letter = fifth_letter
        letters.append(sixth_letter)
        seventh_letter = "s"
        letters.append(seventh_letter)
        eighth_letter = random.choice("ia")
        letters.append(eighth_letter)
        word = "".join(letters)
        if word not in WORDS_SIMPLE:
            WORDS_SIMPLE.append(word)


def create_word_avantgarde(modeString):
    for i in range(0, MAX_MAGIC_LEN):
        letters = []
        prefix = random.choice(PREFIXES)
        first_letter = random.choice("bpm")
        letters.append(first_letter)
        second_letter = random.choice("ia")
        letters.append(second_letter)
        third_letter = random.choice("bp")
        letters.append(third_letter)
        fourth_letter = third_letter
        letters.append(fourth_letter)
        fifth_letter = "s"
        letters.append(fifth_letter)
        sixth_letter = random.choice("ia")
        letters.append(sixth_letter)
        word = prefix + "".join(letters)
        if word not in WORDS_AVANGARDE:
            WORDS_AVANGARDE.append(word)



def output_words(li):
    total_length = len(WORDS_SIMPLE) or len(WORDS_AVANGARDE)
    sleep_time = random.randint(0, 1)/2147483647
    with alive_bar(total_length, calibrate=5, spinner="arrows") as bar:
        for item in li:
            time.sleep(sleep_time)
            bar()
    print()
    for item in li:
        time.sleep(sleep_time)
        print(item, end="... ", flush=True)
    print('\n\n\x1b[6;30;42m' + 'C + M + B 2o21!' + '\x1b[0m')
    print("\na bapśmieni...? a papsi...?")


if __name__ == '__main__':
    main()
