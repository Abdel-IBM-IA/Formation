def produitEntierIntervalle(nb1, nb2):
    """Calcul le produit des entiers compris entre deux entiers naturels positifs
    Renvoie la valeur NotImplemented si les bornes ne sont pas des entiers naturels positifs ou null"""
    if isinstance(nb1, int) and isinstance(nb2, int) and 0 < nb1 and 0 < nb2:
        result = 1
        if nb1 <= nb2:
            for i in range(nb1, nb2):
                result = result * i
        else:
            for i in range(nb2, nb1):
                result = result * i
        return result
    else:
        return NotImplemented


nb1 = 4
nb2 = 6
print(produitEntierIntervalle(nb1, nb2))

nb1 = 5
nb2 = 3
print(produitEntierIntervalle(nb1, nb2))

nb1 = -1
nb2 = -1
print(produitEntierIntervalle(nb1, nb2))

nb1 = 1
nb2 = None
print(produitEntierIntervalle(nb1, nb2))
