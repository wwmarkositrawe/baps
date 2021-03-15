import random
import time
import os

os.system('')

MAX_LEN = 10000
WORDS_SIMPLE = []
WORDS_AVANGARDE = []
PREFIXES = ['pane', 'mono', 'dyne', 'mini', 'mine', 'tele', 'poli', 'semi',
            'mane', 'tone', 'pine', 'solo', 'pupu', 'titi', 'mumu', 'pipi',
            'para', 'nima', 'mana', 'tera', 'tra', 'pra', 'sra', 'fra', 'bra',
            'mra', 'bry', 'pry', 'sry']


def esc(code):
    return f'\033[{code}m'


def main():
    select_mode()


def select_mode():
    modeString = input(
        "by chciałeś/lubiałeś w trybie podstawowym (0), czy dla cwaniaka (1) " +
        "w ramach tzw. trybu premp, powiedz szczerze: ")
    if modeString in ("w trybie podstawowym", "0"):
        create_word_basic(modeString)
        output_words(WORDS_SIMPLE)
    elif modeString in ("dla cwaniaka", "1", "premp"):
        create_word_avantgarde(modeString)
        output_words(WORDS_AVANGARDE)
    else:
        print(esc('31;1;4') + ("że co robi?") + esc(0) + ' cim oyunu \n')


def create_word_basic(modeString):
    for i in range(0, MAX_LEN):
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
    for i in range(0, MAX_LEN):
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
    for i in range(len(li)):
        print(li[i], end="... ", flush=True)
        time.sleep(0.01)
    print('\x1b[6;30;42m' + 'C + M + B 2o21!' + '\x1b[0m')


if __name__ == '__main__':
    main()
