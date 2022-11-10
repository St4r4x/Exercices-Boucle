# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:55:50 2022

@author: st4r4x
"""

# Exercice 8 :

liste1 = [1, 4, 6, 7, 4, 0, 1, 2, 3, 5, 0, 6, 7]
cpt = 0
for i in liste1:
    print(i)
    if i == 0:
        print("Un 0 a été trouvé !")
        print(f"indice {cpt}")
        break
    cpt += 1

liste_temp = []
for n in range(len(liste1)):
    if n+2 > len(liste1)-1:
        continue
    elif liste1[n+1] == 0:
        continue
    else:
        liste_temp.append(liste1[n+2]/liste1[n+1])
