# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:34:38 2023

@author: bapti
"""
import random
import common
import itertools


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global possibleComb
    global LastComb
    global first_try
    possibleComb = set(
        (itertools.product([x for x in common.COLORS], repeat=common.LENGTH)))
    LastComb = random.choice(tuple(possibleComb))
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
    if first_try:
        first_try = False
        return ''.join(LastComb)

    possibleComb = common.maj_possibles(possibleComb, LastComb, evaluation_p)
    LastComb = random.choice(tuple(possibleComb))
    return ''.join(LastComb)


