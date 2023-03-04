# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:10:27 2023

@author: bapti
"""

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus


def evaluation(comb_ev, comb_ref):  # verif avec tuple et str
    assert len(comb_ev) == len(comb_ref) == LENGTH
    if type(comb_ev) == str or type(comb_ref) == str:  # str to list
        comb_ev = list(comb_ev)
        comb_ref = list(comb_ref)

    comb_ev_copy = comb_ev.copy()
    comb_ref_copy = comb_ref.copy()
    right = 0
    wrong = 0

    for i in range(len(comb_ev)):
        if comb_ev[i] == comb_ref[i]:
            right += 1
            comb_ev_copy.remove(comb_ev[i])
            comb_ref_copy.remove(comb_ref[i])

    for i in range(len(comb_ev_copy)):
        if comb_ev_copy[i] in comb_ref_copy:
            wrong += 1
            comb_ref_copy.remove(comb_ev_copy[i])
    return right, wrong


print(evaluation('MMVB', 'BMMV'))


def test_driven(data):
    for k, v in data.items():
        if evaluation(k[0], k[1]) != (v[0], v[1]):
            print(k, v, evaluation(k[0], k[1]))


data_driven0 = {('OVOJ', 'NNBN'): (0, 0), ('RNNB', 'VRBV'): (0, 2), ('NBVB', 'RNJO'): (0, 1), ('MJNO', 'VNVB'): (0, 1), ('JBBJ', 'ONJM'): (0, 1), ('MJMJ', 'MMJO'): (1, 2), ('BVNR', 'JJVR'): (1, 1), ('RVON', 'VNMN'): (1, 1), ('ONJO', 'BJBB'): (0, 1), ('NROB', 'OJRV'): (
    0, 2), ('BRVM', 'NROM'): (2, 0), ('JROR', 'ONOJ'): (1, 1), ('VNBB', 'VOBM'): (2, 0), ('BNJM', 'VRNN'): (0, 1), ('JBRR', 'RBJR'): (2, 2), ('BOBN', 'NRJB'): (0, 2), ('NJMR', 'BNMN'): (1, 1), ('VVNB', 'OMJO'): (0, 0), ('RMMB', 'VONN'): (0, 0), ('VVJM', 'VORV'): (1, 1)}
data_driven1 = {('MMVB', 'BMMV'): (1, 3), ('VVNJ', 'MBRV'): (0, 1), ('BVJB', 'VNBJ'): (0, 3), ('NBRN', 'JVBB'): (0, 1), ('BVVO', 'RONN'): (0, 1), ('JMBN', 'JNRM'): (1, 2), ('OBOO', 'VBOO'): (3, 0), ('ONBO', 'NRJV'): (0, 1), ('VBVV', 'VNRR'): (1, 0), ('OBMB', 'JMNJ'): (
    0, 1), ('VMNO', 'BNMO'): (1, 2), ('RVRB', 'VNRJ'): (1, 1), ('OOVV', 'VMBM'): (0, 1), ('ORJN', 'VMNM'): (0, 1), ('OVBM', 'BNMR'): (0, 2), ('MBOV', 'ROOM'): (1, 1), ('BOMJ', 'JORV'): (1, 1), ('BVVN', 'NOBN'): (1, 1), ('NJNM', 'BJJN'): (1, 1), ('BNOV', 'ORJO'): (0, 1)}

test_driven(data_driven1)
