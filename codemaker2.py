# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:30:41 2023

@author: bapti
"""

import sys
import random
import common  # N'utilisez pas la syntaxe "from common import XXX"
import itertools


def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = 'ROBR'
    global possibleComb
    possibleComb = set(
        (itertools.product([x for x in common.COLORS], repeat=common.LENGTH)))
    LastComb = random.choice(tuple(possibleComb))
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


# def evaluation_partielle(solution, combinaison):
#     if len(solution) != len(combinaison):
#         sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")

#     return common.evaluation(combinaison, solution)


def codemaker(combinaison):  # fusion de codemaker et evaluation partielle
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument)
    """
    global solution
    global possibleComb
    dicoComb = {}

    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    for possibleSol in possibleComb:  # regroupement eva similaire
        possibleEva = common.evaluation(possibleSol, combinaison)
        if possibleEva not in dicoComb:
            dicoComb[possibleEva] = set()
            dicoComb[possibleEva].add(possibleSol)
        else:
            dicoComb[possibleEva].add(possibleSol)
    maxLengthEva = max(dicoComb.values(), key=lambda x: len(x))

    solution = random.choice(tuple(maxLengthEva))
    eva = common.evaluation(combinaison, solution)
    possibleComb = common.maj_possibles(
        possibleComb, combinaison, eva)

    return eva
