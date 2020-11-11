def isBissextileYear(annee) :
    if isinstance(annee, int) :
        if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0) :
            print("L'annee "+str(annee)+" est une annee bissextile!")
        else :
            print("L'annee "+str(annee)+" n'est pas une annee bissextile!")
    else :
        print("La saisie est erronnée, veuillez saisir un nombre entier pour l'année :")


isBissextileYear(2000)
isBissextileYear(1900)
isBissextileYear(2008)
isBissextileYear("Noefene")
isBissextileYear(None)

