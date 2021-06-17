import random
import os
import click
import sys
import numpy as np
import time
from alive_progress import alive_bar, config_handler, bouncing_spinner_factory

config_handler.set_global(length="35", bar="smooth",
                          force_tty=False, enrich_print=True)
# hng_spinner = bouncing_spinner_factory('🛴', 10, hiding=False)
os.system('')  # allows to print ANSI codes in terminal

MAX_MAGIC_LEN = 10000
WORDS_SIMPLE = []
WORDS_AVANGARDE = []
PREFIXES = ['pane', 'mono', 'dyne', 'mini', 'mine', 'tele', 'poli', 'semi',
            'mane', 'tone', 'pine', 'solo', 'pupu', 'titi', 'mumu', 'pipi',
            'para', 'nima', 'mana', 'tera', 'tite', 'pima', 'piba', 'breś',
            'tra', 'pra', 'sra', 'fra', 'bra', 'mra', 'bry', 'pry', 'sry',
            'cim', 'pre', 'sraj', 'preś', 'miau', 'sple', 'sper', 'miaumu',
            'a', 'plene', 'trata']

global li
li = []


@click.group(help="CLI app to create words meeting certain conditions")
def cli():
    pass


@cli.command("mode")
@click.pass_context
@click.option('--mode', type=click.Choice(['baps', 'premp'],
                                          case_sensitive=False),
              prompt="\nHEJ HEJ. By chciałeś/lubiałeś w trybie podstawowym (baps), czy dla cwaniaka (premp)")
def select_mode(ctx, mode):
    if mode == 'baps':
        create_word_basic()
        output_words(ctx, 'baps', WORDS_SIMPLE)
    elif mode == 'premp':
        create_word_avantgarde()
        output_words(ctx, 'premp', WORDS_AVANGARDE)


def output_words(ctx, mode, li):
    try:
        limit = click.prompt('ile chcesz wyrazow cwaniaku [0-{}]: '.format(len(li)),
                             type=click.IntRange(0, len(li)), default=20)
        click.echo('\n')
        with alive_bar(limit, calibrate=4, spinner="arrows") as bar:
            for item in range(limit):
                bar()

        click.echo('\n')
        
        for i in range(0, limit):
            click.echo(click.style("{}: {}".format(i, li[i]), fg=random_color(),
                                   bg=random_color(), bold=True, reset=True))

            # click.echo("{}: ".format(i) + click.style("{}".format(li[i]), fg=random_color(),
            #                        bg=random_color(), bold=True, reset=True))

        click.echo()
        click.echo(click.style('C + M + B 2o21!', italic=True, reset=True))
        click.echo()
        click.echo(click.style("BYYY", reverse=True, reset=True))
        click.echo()
        click.echo(click.style("a bapśmieni?",
                               strikethrough="True", reset=True))
    except IndexError:
        limit = 20


def random_color():
    # levels = range(32, 256, 32)
    # return tuple(random.choice(levels) for _ in range(3))


    # return [random.randint(0, 255),
    #                  random.randint(0, 255), random.randint(0, 255)]


    return tuple(np.random.randint(256, size=3))

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
        if word not in WORDS_SIMPLE:
            WORDS_SIMPLE.append(word)
        if len(WORDS_SIMPLE) == possibilities:
            finished = True
    li = WORDS_SIMPLE
    return li


def create_word_avantgarde():
    # possibilities =  len(PREFIXES) * (3 * 2 * 2 * 1 * 1 * 2) = 43 * 24 = 1032
    possibilities = len(PREFIXES) * 24
    finished = False
    while not finished:
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
        if len(WORDS_AVANGARDE) == possibilities:
            finished = True
    li = WORDS_AVANGARDE
    return li


if __name__ == '__main__':
    cli(obj={})
