def decaleCircDroite(uneList):
    """ Réalise le décalage circulaire vers la droite d’un tableau d’entiers"""
    print(decaleCircDroite.__doc__)
    print("Ma liste avant decalage : ")
    print(uneList)
    # Teste la validite de la liste
    if uneList is not None:
        uneList.insert(0, uneList[-1])
        # Inserè le dernier élément en debut de liste indice 0
        uneList.pop(-1)
        # Suppression de l'élément d'index -1 (dernier)
        print("Ma liste aprés decalage : ")
        print(uneList)
        return uneList
    else:
        return NotImplemented


testList = [10, 21, 30, 45, 26, 17, 22, 13, 11, 4, 9, 3, 5, 7, 32, 43]
decaleCircDroite(testList)
