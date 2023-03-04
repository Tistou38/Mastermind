# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:31:22 2023

@author: bapti
"""


import common
import itertools


def init():
    global possibleComb
    possibleComb = possibleComb = set(
        (itertools.product([x for x in common.COLORS], repeat=common.LENGTH)))


def check_codemaker(log):
    global possibleComb
    possibleComb = possibleComb = set(
        (itertools.product([x for x in common.COLORS], repeat=common.LENGTH)))
    comb = []
    eva = []
    with open(log, 'r') as f:  # formatage data
        l = f.readlines()
        for ligne in l:
            if ',' not in ligne:
                comb_formate = ligne.strip()
                comb_formate = tuple(comb_formate)
                comb.append(comb_formate)
            else:
                ev_formate = ligne.strip()
                ev_formate = tuple(map(int, ev_formate[1:-1].split(',')))
                eva.append(ev_formate)

    for k in range(1, len(comb)):
        possibleComb = common.maj_possibles(possibleComb, comb[k-1], eva[k-1])
        if comb[k] not in possibleComb:
            return 'Triche'

    return 'ok'


print(check_codemaker(
    "G:\Mon Drive\Prepa des INP\CPP 2A\Informatique\Tronc commun\matermind\log\log.txt"))
