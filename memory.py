# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:45:29 2023

@author: bapti
"""
import play as p
import codemaker1
import codemaker2
import codebreaker0
import codebreaker1
import codebreaker2
from tqdm import tqdm
import matplotlib.pyplot as plt


def repeat_hist(n):  # run n-fold a game
    t = []
    for _ in tqdm(range(n)):
        t.append(p.play(codemaker2, codebreaker2))
    return t


plt.hist(repeat_hist(100), color=['grey'], bins=20, hatch='', label=['liste'],
         histtype='barstacked')
plt.ylabel("Number of occurrences")
plt.xlabel("Nombre d'essais")
plt.title("Histogramne nombre d'essais ")
plt.tight_layout()
plt.show()
