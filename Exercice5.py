# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:02:54 2022

@author: st4r4x
"""

# Exercice 5 :


def trouverMultiple(mini, maxi):
    liste = []
    for i in range(mini, maxi):
        if i % 5 == 0 and i % 3 == 0 and i % 7 == 0:
            liste.append(i)
    return liste


print(trouverMultiple(1, 1000))
print(sum(trouverMultiple(1, 1000)))
