# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:45:47 2023

@author: bapti
"""
import random
import common
import itertools
import tqdm


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global possibleComb
    global LastComb
    global first_try
    global AllComb
    possibleComb = set(
        (itertools.product([x for x in common.COLORS], repeat=common.LENGTH)))
    LastComb = random.choice(tuple(possibleComb))
    AllComb = possibleComb.copy()
    first_try = True
    return possibleComb, LastComb


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global LastComb
    global possibleComb
    global first_try
    global AllComb

    AllEva = common.scores_possibles()
    print(AllEva)

    if first_try:
        first_try = False
        return ''.join(LastComb)
    compteur = 0
    MaxComb = {}

    for comb in AllComb:
        AllDonnerPossible = []
        for eva in AllEva:
            # Pour chaque comb on a l'ensemble donner possible le plus grand possible associé a une des eva possible. Il suffit de prendre la comb avec le plus petit ensemble
            AllDonnerPossible.append(common.donner_possibles(comb, eva))

        MaxComb[comb] = max(AllDonnerPossible, key=lambda x: len(x))
        compteur += 1
        print(compteur)
    MinComb = min(MaxComb.items(), key=lambda x: len(x[1]))[0]
    return MinComb


init()
first_try = False
print(codebreaker((1, 2)))
