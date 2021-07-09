import random
import os
import click
import sys
import time
import colorama  # ensuring color support
import colorsys
import datetime
import numpy as np
from alive_progress import alive_bar, config_handler, bouncing_spinner_factory

colorama.init()  # ensuring color support
click.clear()
config_handler.set_global(length="35", bar="smooth",
                          force_tty=False, enrich_print=True)
# hng_spinner = bouncing_spinner_factory('🛴', 10, hiding=False)
os.system('')  # allows to print ANSI codes in terminal

words_simple = []
words_avangarde = []
prefixes = ['pane', 'mono', 'dyne', 'mini', 'mine', 'tele', 'poli', 'semi',
            'mane', 'tone', 'pine', 'solo', 'pupu', 'titi', 'mumu', 'pipi',
            'para', 'nima', 'mana', 'tera', 'tite', 'pima', 'piba', 'breś',
            'tra', 'pra', 'sra', 'fra', 'bra', 'mra', 'bry', 'pry', 'sry',
            'cim', 'pre', 'sraj', 'preś', 'miau', 'sple', 'sper', 'miaumu',
            'a', 'plene', 'trata']

family_roles = ['babki', 'babki cioteczne', 'babki macierzyste', 'babki ojczyste',
                'babki po kądzieli', 'babki po mieczu', 'babki stryjeczne',
                'babki', 'bliźniaki', 'bracia', 'bracia cioteczni',
                'bracia stryjeczni', 'bracia wujeczni', 'bratankowie',
                'bratanice', 'bratowe', 'ciocie', 'cioteczne siostry',
                'cioteczni bracia', 'ciotki', 'córki', 'dziadki',
                'dziadki cioteczni', 'dziadki macierzyści', 'dziadki ojczyści',
                'dziadki po kądzieli', 'dziadki po mieczu', 'dziadki stryjeczni',
                'dziewierze', 'jątrwie', 'kuzyni', 'kuzynki', 'kuzynostwo',
                'macochy', 'małżonkowie', 'mamy', 'matki', 'mężowie',
                'naciotkowie', 'ojce', 'ojczymy', 'pasierby', 'pasierbice',
                'pociotki', 'prababki', 'pradziady', 'prawnuczki', 'prawnuki',
                'przybrane matki', 'przybrane ojce', 'przyrodnie siostry',
                'przyrodni bracia', 'rodzeństwo', 'rodzeństwo cioteczne',
                'rodzeństwo stryjeczne', 'rodzeństwo wujeczne', 'rodzice',
                'siostry', 'siostry cioteczne', 'siostry stryjeczne',
                'siostry wujeczne', 'siostrzenice', 'siostrzeńcy', 'stryjowie',
                'stryjkowie', 'stryjenki', 'stryje', 'stryjostwo', 'swachny',
                'swaty', 'swatowe', 'syny', 'synowe', 'szwagry', 'szwagierki',
                'świekry', 'świekra', 'teściowe', 'teście', 'wnuczki', 'wnuki',
                'współmałżonkowie', 'wujostwo', 'wujki', 'zięciowie', 'żony',
                'homokomando']

prefixes_count = 1

global li
li = []

MIN_PRE = 1
MAX_PRE = 3


def set_prefix():
    return random.choice(prefixes)


@click.group(help="CLI app to create words meeting certain conditions")
def cli():
    pass


@cli.command("mode")
@click.pass_context
@click.option('--mode', help="w jakim trybie utworzyc wyrazy",
              type=click.Choice(['baps', 'premp'], case_sensitive=False),
              prompt="\nHEJ HEJ. By chciałeś/lubiałeś w trybie podstawowym (baps), czy dla cwaniaka (premp)")
def select_mode(ctx, mode):
    global prefixes_count
    prefixes_count = 1
    if mode == 'baps':
        create_word_basic()
        output_words(ctx, 'baps', words_simple)
    elif mode == 'premp':
        while True:
            try:
                prefixes_count = int(
                    input('ile chcesz przedrostków cwaniaku [{}-{}]: '.format(MIN_PRE, MAX_PRE)))
                if prefixes_count < MIN_PRE:
                    print('jeszcze zlotowke')
                elif prefixes_count > MAX_PRE:
                    print('za duzo chcialbys wiedziec')
                else:
                    break
            except TypeError:
                print('nie tak jak trzeba :(')
            except ValueError:
                print('zapytam jeszcze raz, czy jestes gotow')
            finally:
                prefixes_count = prefixes_count
        create_word_avantgarde()
        output_words(ctx, 'premp', words_avangarde)


def output_words(ctx, mode, li):
    with click.open_file('log.txt', 'a', encoding='UTF-8') as f:
        try:
            limit = click.prompt('ile ma byc cwaniaku [0-{}]: '.format(len(li)),
                                 type=click.IntRange(0, len(li)), default=20)

            f.write("*****{}***\n".format(datetime.datetime.now()))
            for i in range(0, limit):
                random_role = random.choice(family_roles)
                click.echo("{}: ".format(i) + click.style("{} {}".format(random_role, li[i]),
                                                          fg=random_color(),
                                                          bg=random_color(),
                                                          bold=True,
                                                          reset=True))
                f.write("{}: {} {}\n". format(i, random_role, li[i]))
            click.echo()

            with alive_bar(limit, calibrate=4, spinner="arrows") as bar:
                for item in range(limit):
                    bar()

            click.echo()
            click.echo(click.style('C + M + B 2o21!', italic=True, reset=True))
            click.echo()
            click.echo(click.style("BYYY", reverse=True, reset=True))
            click.echo()
            click.echo(click.style("a bapśmieni?\n",
                                   strikethrough="True", reset=True))
            f.write("\n")

        except IndexError:
            limit = 20


def random_color():
    # levels = range(32, 256, 32)
    # return tuple(random.choice(levels) for _ in range(3))

    # return [random.randint(0, 255),
    #                  random.randint(0, 255), random.randint(0, 255)]

    return tuple(np.random.randint(256, size=3))
    # h, s, l = random.random(), 1.2 + random.random()/0.56, 1.03 + random.random()/6.5
    # r, g, b = [int(256*i) for i in colorsys.hls_to_rgb(h, l, s)]
    # return (r, g, b)


def create_word_basic():
    # possibilities = 3 * 2 * 3 * 1 * 2 * 1 * 1 * 2 = 72
    possibilities = 72
    finished = False
    while not finished:
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
        if word not in words_simple:
            words_simple.append(word)
        if len(words_simple) == possibilities:
            finished = True
    li = words_simple
    return li


def create_word_avantgarde():
    # possibilities =  len(PREFIXES) * (3 * 2 * 2 * 1 * 1 * 2) = 43 * 24 = 1032
    possibilities = len(prefixes) * 24
    finished = False
    while not finished:
        letters = []
        prefix = random.choice(prefixes)
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

        cnt = 0
        word = ""
        while cnt < prefixes_count:
            word += set_prefix()
            cnt += 1
        word += "".join(letters)

        if word not in words_avangarde:
            words_avangarde.append(word)
        if len(words_avangarde) == possibilities:
            finished = True
    li = words_avangarde
    return li


if __name__ == '__main__':
    cli(obj={})
