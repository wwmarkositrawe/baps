import random
import time


def select_mode():
    modeString = input(
        "by chciałeś/lubiałeś w trybie podstawowym (0), czy dla cwaniaka (1) ")
    if modeString == "w trybie podstawowym" or modeString == "0":
        while True:
            print(create_word_basic() + "\n")
            time.sleep(1)
    elif modeString == "dla cwaniaka" or modeString == "1":
        while True:
            print(create_word_avantgarde() + "\n")
            time.sleep(1)
    print("że co robi?" + "\n")
    select_mode()


def create_word_basic():
    first_letter = random.choice("bpm")
    second_letter = random.choice("ia")
    third_letter = random.choice("bpm")
    fourth_letter = second_letter
    fifth_letter = random.choice("bp")
    sixth_letter = fifth_letter
    seventh_letter = "s"
    eighth_letter = random.choice("ia")
    wyraz = ""
    word = first_letter + second_letter + third_letter + fourth_letter + \
        fifth_letter + sixth_letter + seventh_letter + eighth_letter
    return word


def create_word_avantgarde():
    prefixes = ['pane', 'mono', 'dyne', 'mini', 'mine',
                'mane', 'tone', 'pine', 'solo', 'pupu', 'titi', 'mumu', 'pipi']
    fifth_letter = random.choice("bpm")
    sixth_letter = random.choice("ia")
    seventh_letter = random.choice("bp")
    eighth_letter = seventh_letter
    nineth_letter = "s"
    tenth_letter = random.choice("ia")
    word = random.choice(prefixes) + fifth_letter + sixth_letter + \
        seventh_letter + eighth_letter + nineth_letter + tenth_letter
    return word


while True:
    select_mode()
