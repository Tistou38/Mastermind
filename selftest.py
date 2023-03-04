#!/usr/bin/env python3
""" Autotests

Ces auto-tests vous permettent de détecter un certain nombre d'erreurs (non-respect des spécifications notamment) élémentaires.
Ils sont *volontairement* incomplets (apprendre à lire et respecter une spécification fait partie des points travaillés à travers le projet) mais vous évitent de partir sur une architecture incorrecte dès les premières questions.
Notez bien que ce script s'arretera à la première erreur rencontrée.
"""

import sys
import os
import re
import traceback


def q1():
    if not os.path.isfile("common.py"):
        print("q1: fichier 'common.py' non trouvé")
        return False
    for pf in os.listdir():
        if pf.endswith(".py"):
            with open(pf, 'r') as f:
                for l in f:
                    if re.search('^ *from +common +import', l):
                        print('fichier {}: la syntaxe "from common import XXX" ne doit pas être utilisée'.format(pf))
                        return False
    import common
    global common
    if common.LENGTH != 4:
        print("Attention, common.LENGTH a été modifié, on remet la valeur par défaut (4) pour ces tests")
        common.LENGTH = 4
    if common.COLORS != ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']:
        print("Attention, common.COLORS a été modifié, on remet la valeur par défaut pour ces tests")
        common.COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
    if 'evaluation' not in dir(common):
        print("q1: fonction 'evaluation' non trouvée dans common.py")
        return False
    try:
        r = common.evaluation('RRVB', 'JORV')
    except:
        print("q1: l'appel à common.evaluation('RRVB', 'JORV') a causé une erreur")
        traceback.print_exc()
        return False
    if type(r) is not tuple or len(r) != 2:
        print("q1: common.evaluation('RRVB', 'JORV') ne renvoie pas un tuple de longueur 2")
        return False
    if r != (0, 2):
        print("q1: common.evaluation('RRVB', 'JORV') ne renvoie pas la valeur attendue")
        return False
    common.LENGTH = 5
    try:
        r = common.evaluation('RVBJN', 'RBVOO')
    except:
        print("q1: l'appel à common.evaluation('RVBJN', 'RBVOO') a causé une erreur\n(common.LENGTH avait été mis à 5 pour ce test)")
        traceback.print_exc()
        return False
    common.LENGTH = 4
    if r != (1, 2):
        print("q1: common.evaluation('RVBJN', 'RBVOO') ne renvoie pas la valeur attendue")
        return False
    return True


def q2():
    if not os.path.isfile('codemaker1.py'):
        print("q2: fichier 'codemaker1.py' non trouvé")
        return False
    import codemaker1
    if 'init' not in dir(codemaker1):
        print("q2: fonction 'init' non trouvée dans 'codemaker1.py'")
        return False
    if 'codemaker' not in dir(codemaker1):
        print("q2: fonction 'codemaker' non trouvée dans 'codemaker1.py'")
        return False
    try:
        codemaker1.init()
    except:
        print("q2: l'appel à 'codemaker1.init()' a causé une erreur")
        traceback.print_exc()
        return False
    try:
        r = codemaker1.codemaker('RRRR')
    except:
        print("q2: l'appel à codemaker1.codemaker('RRRR') a causé une erreur")
        traceback.print_exc()
        return False
    if type(r) is not tuple or len(r) != 2:
        print("q2: codemaker1.codemaker('RRRR') ne renvoie pas un tuple de longueur 2")
        return False
    return True


def q5():
    global common
    if 'donner_possibles' not in dir(common):
        print('q5: fonction donner_possibles non trouvée dans common.py')
        return False
    try:
        r = common.donner_possibles('RRRR', (1, 0))
    except:
        print("q5: l'appel à common.donner_possibles('RRRR', (1, 0)) a causé une erreur")
        traceback.print_exc()
        return False
    if type(r) is not set:
        print("q5: donner_possibles('RRRR', (1, 0)) ne renvoie pas un set")
        return False
    return True


def q6():
    global common
    if 'maj_possibles' not in dir(common):
        print('q6: fonction maj_possibles non trouvée dans common.py')
        return False
    return True


if __name__ == '__main__':
    if q1() and q2() and q5() and q6():
        print("Auto-tests élémentaires réussis (cela ne garantit pas que vos programmes sont corrects)")
    else:
        print("Échec des auto-tests élémentaires (arrêt à la première erreur rencontrée)")
