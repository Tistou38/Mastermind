# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 17:58:25 2023

@author: bapti
"""

import random


COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']

D = {}
for i in range(20):
    comb_ev = ''
    comb_ref = ''
    for i in range(4):
        ev = random.randrange(0, 7)
        ref = random.randrange(0, 7)
        comb_ev += COLORS[ev]
        comb_ref += COLORS[ref]

    print(comb_ev, comb_ref)
    (right, wrong) = input()
    D[comb_ev, comb_ref] = (right, wrong)

print(D)

d = {('OVOJ', 'NNBN'): (0, 0), ('RNNB', 'VRBV'): (0, 2), ('NBVB', 'RNJO'): (0, 1), ('MJNO', 'VNVB'): (0, 1), ('JBBJ', 'ONJM'): (0, 1), ('MJMJ', 'MMJO'): (1, 2), ('BVNR', 'JJVR'): (1, 1), ('RVON', 'VNMN'): (1, 1), ('ONJO', 'BJBB'): (0, 1), ('NROB', 'OJRV'): (
    0, 2), ('BRVM', 'NROM'): (2, 0), ('JROR', 'ONOJ'): (1, 1), ('VNBB', 'VOBM'): (2, 0), ('BNJM', 'VRNN'): (0, 1), ('JBRR', 'RBJR'): (2, 2), ('BOBN', 'NRJB'): (0, 2), ('NJMR', 'BNMN'): (1, 1), ('VVNB', 'OMJO'): (0, 0), ('RMMB', 'VONN'): (0, 0), ('VVJM', 'VORV'): (1, 1)}
