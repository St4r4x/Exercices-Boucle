# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:07:24 2022

@author: st4r4x
"""

# Exercice 2 :

vie = 10
espoir = 0
while vie > 0:
    while espoir < 5:
        espoir += 1
        print("tant qu'il y a la vie")
    print("on dit toujours y a espoir")
    vie -= 1
print("Magic System")

# Réponse 1 : espoir vaut 5 à la fin du programme
# Réponse 2 : vie vaut 0 à la fin du programme
# Réponse 3 : elle va apparaitre 5 fois
# Réponse 4 : elle va apparaitre 5 fois

for i in range(6):
    for j in range(0, 4, 4):
        print("Feel the magic in the air")
        print("Allez, allez, allez")
        for m in range(0, 2, 2):
            print("Levez les mains en l'air")
            print("Allez, allez, allez")

print("Magic System")
