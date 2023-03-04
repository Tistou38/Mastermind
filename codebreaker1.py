# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:18:18 2023

@author: bapti
"""
import random
import common  #


def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global A
    A = []
    return


def codebreaker(evaluation_p):
    """
    L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
    combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
    partie). Cette version triviale n'utilise pas cette information, puisqu'
    elle joue au hasard.
    """
    global A
    choice = random.choices(common.COLORS, k=common.LENGTH)
    while choice in A:
        choice = random.choices(common.COLORS, k=common.LENGTH)
    A.append(choice)
    return ''.join(choice)
