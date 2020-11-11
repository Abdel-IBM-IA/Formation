from random import random


def initialiseTableauManuel(tableau):
    n = int(input("Saisir le nombre d'éléments à insérer dans le tableau :"))
    for i in range(0, n):
        tableau.append(int(input("Saisissez la valeur ", i + 1, " :")))


def initialiseTableauAuto(tableau):
    n = int(input("Saisir le nombre d'éléments à insérer dans le tableau :"))
    for i in range(0, n):
        tableau.append(int(random(0,100)))