def strsaisiemanuelle() :
    masaisie = str(input("Veuillez saisir une chaine : "))
    return masaisie


def middleofmystring(unechaine) :
    indice = len(unechaine) // 2
    return indice


def extractcases(unechaine) :
    """
Extrait tous les caractères minuscule et majuscule d'une chaine
    :param unechaine:
    :return List[(liste_minuscule, string),(liste_majuscule, string)]:
    """
    minustring = ""
    majustring = ""
    for charcourant in unechaine :
        if 'a' <= charcourant <= 'z' :
            minustring += charcourant
        else :
            if 'A' <= charcourant <= 'Z' :
                majustring += charcourant
    return [minustring, majustring]


def counttypeofchar(unechaine) :
    """
Compter toutes les lettres, les chiffres et les caractères spéciaux présents dans une chaine de caractères
    :param unechaine:
    :return List[(string,int)]:
    """
    nblettres = 0
    nbchiffres = 0
    nbspecialchar = 0
    for charcourant in unechaine :
        if 'a' <= charcourant <= 'z' or 'A' <= charcourant <= 'Z' :
            nblettres += 1
        else :
            if '0' <= charcourant <= '9' :
                nbchiffres += 1
            else :
                nbspecialchar += 1
    return [("nb_lettres", nblettres), ("nb_chiffres", nbchiffres), ("nb_specialchar", nbspecialchar)]


def checkalloneinother(string1, string2) :
    """
Vérifier que toutes les lettres d'une chaine de caractères se trouvent dans une autre chaine de caractère
    """

    toustrouve=True
    for charcourant in string1 :
        if charcourant in string2 :
            unpastrouve = False
        else :
            toustrouve = False
    return toustrouve


def countnbOccurence(string1, string2):
    """
Donner le nombre d’occurrences de la chaine « USA » dans une chaine donnée en ignorant la casse
    """
    upstring1 = string1.upper()
    upstring2 = string2.upper()

    result = upstring1.count(upstring2)
    return result

