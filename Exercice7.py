# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:39:18 2022

@author: st4r4x
"""

# Exercice 7 :


def voyagerPied(nombre_km):
    km_parcouru = 0  # les km parcourus
    temps_passe = 0  # le temps passé en jours
    argent_depense = 0  # argent dépensé en euros
    while km_parcouru <= nombre_km:
        km_parcouru += 20
        temps_passe += 1
        argent_depense += 10
    return temps_passe, argent_depense


def voyagerVoiture(nombre_km):
    km_parcouru = 0  # les km parcourus
    temps_passe = 0  # le temps passé en jours
    argent_depense = 0  # argent dépensé en euros
    while km_parcouru <= nombre_km:
        km_parcouru += 1000
        temps_passe += 1
        argent_depense += 100
    return temps_passe, argent_depense


def voyagerVelo(nombre_km):
    km_parcouru = 0  # les km parcourus
    temps_passe = 0  # le temps passé en jours
    argent_depense = 0  # argent dépensé en euros
    while km_parcouru <= nombre_km:
        km_parcouru += 100
        temps_passe += 1
        argent_depense += 10
    return temps_passe, argent_depense


def voyagerAvion(nombre_km):
    km_parcouru = 0  # les km parcourus
    temps_passe = 0  # le temps passé en jours
    argent_depense = 0  # argent dépensé en euros
    while km_parcouru <= nombre_km:
        km_parcouru += 6000
        temps_passe += 1
        argent_depense += 500
    return temps_passe, argent_depense


print(voyagerAvion(40075))
