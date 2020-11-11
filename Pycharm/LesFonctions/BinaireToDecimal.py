def bin2Dec(unBinaire):
    """ Permet de convertir une chaîne de caractères contenant la représentation binaire d’un nombre
    (codage entier naturel) en sa représentation décimale. """
    print(bin2Dec.__doc__)
    nBin = 0
    # Teste la validite du nombre bianire
    if unBinaire.isdigit():
        strMonBinaire = str(unBinaire)
        print(strMonBinaire)
        return int(strMonBinaire, 2)
    else:
        return NotImplemented


testBinaire = 100101
bin2Dec(testBinaire)
