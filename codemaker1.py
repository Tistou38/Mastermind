#!/usr/bin/env python3

import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def evaluation_partielle(solution, combinaison):
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")

    return common.evaluation(combinaison, solution)


def codemaker(combinaison):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    return evaluation_partielle(solution, combinaison)
