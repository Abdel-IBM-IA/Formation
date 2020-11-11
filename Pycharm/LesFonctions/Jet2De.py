from random import *


def jet2De() :
    de = randint(1, 6)
    print("lancer: " + str(de))


jet2De()


def jetNDe(nb) :
    if isinstance(nb, int) :
        for cpt in range(nb) :
            de = randint(1, 6)
            print("lancer " + str(cpt + 1) + ": " + str(de))
        print("\n")
    else :
        print("La saisie est erronnée, veuillez saisir un nombre entier pour le nombre de lancer de dé(s) :")


print("jet de 2 dés")
jetNDe(2)
print("jet de 3 dés")
jetNDe(3)

