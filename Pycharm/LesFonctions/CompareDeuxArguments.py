import unicodedata


def oterlesaccents(ch) :
    """Supprime les accents sans changer la casse (majuscules et minuscules)"""
    r = u""
    for car in ch :
        if car == u"\xA0" :  # Pour conserver les espaces (espaces insécables également)
            r += car
        else :
            carNFKD = unicodedata.normalize('NFKD', car)
            r += carNFKD[0]
    return r


def compare(a, b) :
    """ Compare les deux arguments passés en entrée
    et affiche un message adapté 'supérieur', 'inférieur' ou 'égal'.
    Prise en compte des entiers, des flottants et des chaînes de caractères.
    """
    result = ""
    # On s'assure que les paramètres sont de même nature pour que la comparaison soit cohérente
    if isinstance(a, str) and isinstance(b, str) :
        # Pour la comparaison de chaines de caractère on adopte l'ordre alphabétique
        # Les accents sont supprimés pour permettre
        aNFKD = oterlesaccents(a)
        bNFKD = oterlesaccents(b)

        if aNFKD.upper() < bNFKD.upper() :  # La casse est prise en compte pour la comparaison
            result = "Dans l'ordre alphabétique '" + a + "' arrive avant '" + b + "'"
        elif aNFKD.upper() > bNFKD.upper() :
            result = "Dans l'ordre alphabétique '" + a + "' arrive aprés '" + b + "'"
        elif a == b :
            result = "La valeur de la chaine de caractère(s) des deux arguments passés est identique : \"" + a + "\""
        else :
            result = "La valeur de la chaine de caractère(s) des deux arguments passés est équivalente : \"" + a + "\" et \"" + b + "\""

    elif isinstance(a, (float, int)) and isinstance(b, (float, int)) :
        # Pour la comparaison de nombres les deux paramètres sont convertis en instance float pour généraliser le cas

        if float(a) < float(b) :
            result = "Le premier paramètre : " + str(a) + " est inférieur au second : " + str(b)
        elif float(a) > float(b) :
            result = "Le premier paramètre : " + str(a) + " est supérieur au second : " + str(b)
        else :
            result = "La valeur numérique des deux arguments passés est identique : " + str(a)

    else :
        # Les deux paramètres ne sont pas de même nature ils ne sont pas comparables !
        result = "Les deux paramètres ne sont pas de même nature, et ne sont pas comparables \ntype a :" + str(
            type(a)) + "\ntype b :" + str(type(b))

    return result


# Tests
print("Comparaison de 'd' et 'd'")
print("Resultat : " + compare('d', 'd'))
print("\n")

print("Comparaison de 's' et 't'")
print("Resultat : " + compare('s', 't'))
print("\n")

print("Comparaison de 't' et 's'")
print("Resultat : " + compare('t', 's'))
print("\n")

print("Comparaison de 'O' et 'P'")
print("Resultat : " + compare('O', 'P'))
print("\n")

print("Comparaison de 'P' et 'O'")
print("Resultat : " + compare('P', 'O'))
print("\n")

print("Comparaison de 'â' et 'A'")
print("Resultat : " + compare('â', 'A'))
print("\n")

print("Comparaison de \"c'est l'été\" et \"C'est l'ete\"")
print("Resultat : " + compare("c'est l'été", "C'est l'ete"))
print("\n")

print("Comparaison de 3 et 5")
print("Resultat : " + compare(3, 5))
print("\n")

print("Comparaison de 9 et 7")
print("Resultat : " + compare(9, 7))
print("\n")

print("Comparaison de -1 et 1")
print("Resultat : " + compare(-1, 1))
print("\n")

print("Comparaison de 3 et 5.5")
print("Resultat : " + compare(3, 5.5))
print("\n")

print("Comparaison de 9.5 et 7")
print("Resultat : " + compare(9.5, 7))
print("\n")

print("Comparaison de -3.3 et -5.5")
print("Resultat : " + compare(-3.3, -5.5))
print("\n")

print("Comparaison de 3 et 3.0")
print("Resultat : " + compare(3, 3.0))
print("\n")

print("Comparaison de 'A' et 1")
print("Resultat : " + compare('A', 1))
print("\n")

print("Comparaison de 'Abc' et 1.5")
print("Resultat : " + compare("Abc", 1.5))
print("\n")
