#!/usr/bin/env python3

import common


def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution

    Attention, il ne *doit* pas être nécessaire de modifier cette fonction 
    pour faire fonctionner vos codemaker et codebreaker (dans le cas contraire,
    ceux-ci ne seront pas considérés comme valables)
    """
    n_essais = 0
    codebreaker.init()
    codemaker.init()
    ev = None
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(
            common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev)
        ev = codemaker.codemaker(combinaison)
        n_essais += 1
        if not quiet:
            print("Essai {} : {} ({},{})".format(
                n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(
                    combinaison, n_essais))
            return n_essais


def play_log(codemaker, codebreaker, quiet=False, log=True):
    """
    Fonction principale de ce programme :
    log de la partie
    """
    n_essais = 0
    codebreaker.init()
    codemaker.init()
    ev = None
    f = open(
        "G:\Mon Drive\Prepa des INP\CPP 2A\Informatique\Tronc commun\matermind\log\log.txt", "w")
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(
            common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev)
        ev = codemaker.codemaker(combinaison)
        n_essais += 1
        if not quiet and log:
            f.write("{}\n({},{})\n".format(combinaison, ev[0], ev[1]))
            print("Essai {} : {} ({},{})".format(
                n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(
                    combinaison, n_essais))

            f.close()
            return n_essais


if __name__ == '__main__':
    # Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :

    # Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :
    import codebreaker2
    import codemaker1

    for i in range(10):
        play_log(codemaker1, codebreaker2)

    #  Faire jouer un humain contre codemaker0.py :
    # import codemaker0
    # import human_codebreaker
    # play(codemaker0, human_codebreaker)

    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    # import codebreaker2
    # import codemaker2
    # play(codemaker2, codebreaker2)

    # Ou encore :
    # import codebreaker1
    # import human_codemaker
    # play(human_codemaker, codebreaker1)
