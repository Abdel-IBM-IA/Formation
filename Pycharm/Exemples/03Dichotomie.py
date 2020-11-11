Liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sup = len(Liste) - 1
inf = 0
x = 11
while inf <= sup:
    middle = (inf + sup) // 2
    if Liste[middle] == x:
        # x a été trouvé son indice est middle
        print("la valeur a été trouvée son indice est : ", middle)
        break

    elif Liste[middle] < x:
        # la valeur recherchée est dans la partie supérieur du tableau
        # => indice inférieur évolue
        inf = middle + 1

    else:
        # la valeur recherchée est dans la partie inférieur du tableau
        # => indice supérieur évolue
        sup = middle - 1
else:
    print("la valeur n'est pas dans le tableau")