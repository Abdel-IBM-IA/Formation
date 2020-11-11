def extract(uneList):
    # Teste la validite de la liste
    if uneList is not None:
        # Teste le type entier pour toutes les occurences
        if all(type(x) == int for x in uneList):
            listNbPair = []
            listNbImpair = []
            for nb in uneList:
                if nb % 2 == 0:
                    listNbPair.append(nb)
                else:
                    listNbImpair.append(nb)
            print("La liste des entiers pair est : ", listNbPair)
            print("La liste des entiers impair est : ", listNbImpair)
        else:
            return NotImplemented
    else:
        return NotImplemented


testList = [10, 21, 30, 45, 26, 17, 22, 13, 11, 4, 9, 3, 5, 7, 32, 43]
print(extract(testList))
