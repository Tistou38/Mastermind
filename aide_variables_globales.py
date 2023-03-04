#!/usr/bin/env python3
"""Quelques exemple pour expliquer et illustrer l'utilisation de variables globales. Exécutez les programmes ci-dessous, et comprenez ce qui se passe :"""

# %% exemple 1
def f():
    x = 3

f()
print(x)  # Erreur ("name 'x' is not defined") : la variable x est locale à la fonction f, c'est à dire qu'elle n'existe pas en dehors de cette fonction

# %% exemple 1 bis
def f():
    x = 3

def g():
    print(x)


f()
g()  # Erreur ("name 'x' is not defined") : pareil que ci-dessus, la variable x est locale à la fonction f

# %% exemple 2

x = 5
def f():
    print(x)

f()  # ça fonctionne, x est une variable globale (qui peut être lue par la fonction f)

# %% exemple 3

x = 5
def f():
    x=3

f()
print(x)  # ça affiche 5 (et non pas 3)

# %% exemple 3 bis

x = 5
def f():
    x = x+1

f()  # Erreur ("local variable 'x' referenced before assignment")

# Conclusion des exemples ci-dessus : par défaut, les variables définies "dans le main" (i.e. en dehors des fonctions) peuvent utilisées *en lecture seulement* par des fonctions (ce sont des variables *globales*). En revanche, par défaut lorsqu'une fonction fait une affectation sur une variable, celle-ci devient automatiquement *locale* à la fonction (et l'accès en lecture par cette fonction à la valeur de la variable définie en dehors de la fonction n'est alors pas possible : ce ne sont en fait plus les mêmes variables).

# Comment faire pour avoir des fonctions qui lisent et *écrivent* dans des variables *globales* ? En utilisant le mot clé "global" :

# %% exemple 4

x=5
def f():
    global x
    x = x+1
    print(x)

f()  # affiche 6
f()  # affiche 7
print(x)  # affiche 7

# %% exemple 4 bis

def f():
    global x
    x = 3

def g():
    global x
    x+=1

f()
g()
print(x)  # affiche 4

# %% exemple 4 ter

def f():
    global x
    x = 3

def g():
    print(x)  # Ici x n'est utilisé qu'en lecture, donc pas besoin du mot clé "global", mais il serait nécessaire pour faire quelque chose comme x+=1

f()
g()  # affiche 3
print(x)  # affiche également 3 : la variable globale est utilisable par toute autre fonction mais aussi dans le main

# Pour finir, notez bien qu'une variable globale est partagée entre plusieurs fonctions du même fichier (et entre plusieurs appels successifs de ces fonctions), mais en aucun cas entre plusieurs fichiers
