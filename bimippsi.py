
import random

def create_word():
    first_letter = random.choice("bpm")
    second_letter = random.choice("ia")
    third_letter = random.choice("bpm")
    fourth_letter = second_letter
    fifth_letter = random.choice("bp")
    sixth_letter = random.choice([fifth_letter, "s"])
    eight_letter = random.choice("ia")
    word = first_letter+second_letter+third_letter+fourth_letter+fifth_letter+sixth_letter+"s"+eight_letter
    return word

word = create_word()
print(word)






