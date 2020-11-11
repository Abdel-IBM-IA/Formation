def estPair2(nb) :

    if isinstance(nb, (int, float)) :
        result = ((nb % 2) == 0)
        print(str(nb) + " est un nombre paire : " + str(result))
    else :
        result = False
        print(str(nb) + " est un nombre paire : " + str(result))
    return result


def estPair(nb) :
    if isinstance(nb, (int, float)) :
        if (nb % 2) == 0 :
            print(str(nb) + " est un nombre pair")
        else :
            print(str(nb) + " est un nombre impair")
    elif nb is None :
        print("La valeur à tester est nulle !")
    else :
        print("La valeur saisie n'est pas un nombre :", nb)


nb = 4
estPair(nb)

nb = 5
estPair(nb)

nb = 2.0
estPair(nb)

nb = 5.0
estPair(nb)

nb = 'e'
estPair(nb)

nb = "azer"
estPair(nb)

estPair(None)