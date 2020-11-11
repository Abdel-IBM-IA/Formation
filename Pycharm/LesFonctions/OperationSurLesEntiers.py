def listeNCarre(nb) :
    if isinstance(nb, int) :
        result = ""
        for cpt in range(nb+1) :
            result += str(cpt*cpt) + " - "
        result = result[:-3] # Supprime les trois derniers caractères
        print(result)
    else :
        print("La saisie est erronnée, veuillez saisir un nombre entier pour le nombre :")


listeNCarre(10)


def produitListeEntier(nb1,nb2) :
    if isinstance(nb1, int) and isinstance(nb2, int) :
        result = ""
        for cpt in range(nb+1) :
            result += str(cpt*cpt) + " - "
        result = result[:-3] # Supprime les trois derniers caractères
        print(result)
    else :
        print("La saisie est erronnée, veuillez saisir un nombre entier pour le nombre :")


listeNCarre(10)
