import re
from statistics import mean

from mytools import middleofmystring, extractcases, counttypeofchar, checkalloneinother, countnbOccurence

chaine1 = "En théorie l'Intelligence Artificielle fait des erreurs que les humains ne feraient pas !"
chaine2 = "beaucoup moins d'erreurs mais elle fait "

machaine = "Il Y A Deux Façons De Faire La Conception D'Un Logiciel. " \
           "Une De Le Rendre Si Simple Qu'Il N'Y A Selon Toute Apparence Aucun Défaut. " \
           "Et L'Autre Si Compliqué Qu'Il N'Y A Pas De Défaut Apparent."


# machainesaisie = strsaisiemanuelle()


###################
# EXO 1
def exo1sub5(unechaine):
    """Exo1 Renvoie les cinq lettres centrales d'une chaine de caractère"""
    print("*** Début Exo 1 ***")
    print(exo1sub5.__doc__)
    middle = len(unechaine) // 2 - 3
    result = unechaine[middle:middle + 5]
    print("Ma chaine : \n", unechaine)
    print(result)
    print("*** Fin Exo 1 ***")
    print("\n")
    return result


exo1sub5(machaine)


###################
# EXO 2
def exo2subinsub(s1, s2):
    """Exo2 Insère une chaine de caractère au milieu d'une autre chaine de caractère"""
    print("*** Début Exo 2 ***")
    print(exo2subinsub.__doc__)
    middle = middleofmystring(s1)
    result = s1[0:middle] + s2 + s1[middle:]
    print("chaine 1 : ", s1)
    print("chaine 2 : ", s2)
    print("Resultat : \n", result)
    print("*** Fin Exo 2 ***")
    print("\n")
    return result


exo2subinsub(chaine1, chaine2)


###################
# EXO 3
def exo3submix2string(s1, s2):
    """Exo3 Extrait le premier, le dernier et le caractère central de deux chaines"""
    print("*** Début Exo 3 ***")
    print(exo3submix2string.__doc__)
    result = s1[0] + s2[0] + s1[middleofmystring(s1)] + s2[middleofmystring(s2)] + s1[-1] + s2[-1]
    print("Mot 1 : ", s1)
    print("Mot 2 : ", s2)
    print("Resultat : ", result)
    print("*** Fin Exo 3 ***")
    print("\n")
    return result


mot1 = "Intelligence"
mot2 = "Artificielle"
exo3submix2string(mot1, mot2)


###################
# EXO 4
def exo4extractcases(unechaine):
    """Exo4 Extrait les majuscules et les minuscules d'une chaine"""
    print("*** Début Exo 4 ***")
    print(exo4extractcases.__doc__)
    myextract = extractcases(unechaine)
    print("Ma chaine : ", unechaine)
    print("Les minuscules : \n", myextract[0])
    print("Les majuscules : \n", myextract[1])
    print("*** Fin Exo 4 ***")
    print("\n")
    return myextract


exo4extractcases(machaine)


###################
# EXO 5
def exo5counttypeofchar(unechaine):
    """Exo5 Compter lettres, chiffres et caractères spéciaux d'une chaine de caractères
    """
    print("*** Début Exo 5 ***")
    print(exo5counttypeofchar.__doc__)
    compteur = counttypeofchar(unechaine)
    print("Ma chaine : ", unechaine)
    print("Nb lettres : ", compteur[0])
    print("Nb chiffres : ", compteur[1])
    print("Nb special char : ", compteur[2])
    print("*** Fin Exo 5 ***")
    print("\n")
    return compteur


chainetest = "N@aiv33e&Ba^yes"
exo5counttypeofchar(chainetest)


###################
# EXO 6
def fusiontwostring(chaine1, chaine2):
    chaine = ""
    for i in range(0, len(chaine1)):
        chaine += chaine1[i]
        chaine += chaine2[-1-i]
    return chaine


def exo6fusion(chaine1, chaine2):
    """Exo6 Crée une chaine S3 en alternant les caractères de S1 et de S2 inversée
    :param chaine1, chaine2:
    :return string:
    """
    print("*** Début Exo 6 ***")
    print(exo6fusion.__doc__)
    result = fusiontwostring(chaine1, chaine2)
    print("Ma première chaine : ", chaine1)
    print("Ma seconde chaine : ", chaine2)
    print("Resultat : ", result)
    print("*** Fin Exo 6 ***")
    print("\n")
    return result


S1 = "Abc"
S2 = "Xyz"
exo6fusion(S1, S2)


###################
# EXO 7
def exo7checkalloneinother(str1, str2):
    """Vérifie que tous les caractères d’une chaine S1 sont présents dans une chaine S2 (peu importe la position)
    :return boolean:
    """
    print("*** Début Exo 7 ***")
    print(exo7checkalloneinother.__doc__)
    result = checkalloneinother(str1, str2)
    print("Ma première chaine : ", str1)
    print("Ma seconde chaine : ", str2)
    print("Tous les caractères de ",str1," sont dans ",str2," : ", result)
    print("*** Fin Exo 7 ***")
    print("\n")
    return result


S1 = "Abce"
S2 = "Xyzbac"
exo7checkalloneinother(S1, S2)


###################
# EXO 8
def exo8nbOccurence(str1, str2):
    """ Donner le nombre d’occurrences de la chaine « USA » dans une chaine donnée en ignorant la casse  """
    print("*** Début Exo 8 ***")
    print(exo8nbOccurence.__doc__)
    result = countnbOccurence(str1, str2)
    print("Ma première chaine : ", str1)
    print("Ma seconde chaine : ", str2)
    print("Nombre d'occurences de ",str2," dans ",str2,"est : ", result)
    print("*** Fin Exo 8 ***")
    print("\n")
    return result


S1 = "azerty fdsqfd AZE dfdAZe  Aze aZe azE AzE "
S2 = "AZE"
exo8nbOccurence(S1, S2)


###################
# EXO 9
def exo9sumandeverageinstring(string1):
    """ Calcule la somme et la moyenne de tous les nombres présents dans une chaine de caractères """
    print("*** Début Exo 9 ***")
    print(exo9sumandeverageinstring.__doc__)
    mesvaleurs = [int(char) for char in string1.split() if char.isdigit()]
    print (mesvaleurs)

    mesvaleurs2=[]
    for caractere in string1.split():
        if caractere.isdigit():
            mesvaleurs2.append(int(caractere))
    print(mesvaleurs2)

    print("Ma somme : ", sum(mesvaleurs))
    print("Ma moyenne : ", mean(mesvaleurs))
    print("*** Fin Exo 9 ***")
    print("\n")


S1 = "English = 78 Science = 83 Math = 68 History = 65"
exo9sumandeverageinstring(S1)


###################
# EXO 10
def exo10sumandeverageinstring(string) :
    """ Compter la fréquence de chaque caractère qui compose une chaine donnée """
    print(" *** Début Exo 10 *** ")
    print(exo10sumandeverageinstring.__doc__)

    dico = {}
    for key in string:
        if key in dico :
            dico[key] += 1
        else :
            dico[key] = 1

    print("Résultat : ", dico)
    print("*** Fin Exo 10 ***")
    print("\n")


S1 = "Appleee"
exo10sumandeverageinstring(S1)


###################
# EXO 11
def exo11inverserunestring(machaine) :
    """ Inverser une chaine de carctères donnée """
    print(" *** Début Exo 11 *** ")
    print(exo11inverserunestring.__doc__)

    print("Ma chaine : ", machaine)

    print("Ma chaine inversée : ", machaine[::-1])
    print("*** Fin Exo 11 ***")
    print("\n")


S1 = "Appleee"
exo11inverserunestring(S1)


###################
# EXO 12
def exo12lastoccurence(machaine,achercher) :
    """ Trouver la dernière position de la chaine Emma dans une chaine donnée """
    print(" *** Début Exo 12 *** ")
    print(exo12lastoccurence.__doc__)

    lastoccur = machaine.rfind(achercher)
    print("dernière occurence : ", lastoccur)

    print("*** Fin Exo 12 ***")
    print("\n")


str1 = "Emma est une data scientist qui programme en Python. Emma travaille chez google."
str2 = "Emma"
exo12lastoccurence(str1,str2)


###################
# EXO 13
def exo13splitterunechaine(machaine) :
    """ Découper une chaine de caractères dont le séparateur est le trait d’union et afficher toutes les sous-chaines
    obtenues """
    print(" *** Début Exo 13 *** ")
    print(exo13splitterunechaine.__doc__)
    print("Ma chaine avant split : ", machaine)
    result = machaine.split('-')

    print("Ma chaine aprés split : ", result)

    print("*** Fin Exo 13 ***")
    print("\n")


str_list = "Emma-est-une-data-scientist"
exo13splitterunechaine(str_list)


###################
# EXO 14
def exo14filtreliste(malist) :
    """ Découper une chaine de caractères dont le séparateur est le trait d’union et afficher toutes les sous-chaines
    obtenues """
    print(" *** Début Exo 14 *** ")
    print(exo14filtreliste.__doc__)
    print("Ma list avant filter : ", malist)

    result = list(filter(None, malist))

    print("Ma chaine aprés filter : ", result)

    print("*** Fin Exo 14 ***")
    print("\n")


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
exo14filtreliste(str_list)


###################
# EXO 15
def exo15filtretring(malist) :
    """ Supprimer toutes les ponctuations et les caractères spéciaux présents dans une chaine donnée """
    print(" *** Début Exo 15 *** ")
    print(exo15filtretring.__doc__)
    print("Ma list avant filter : ", malist)

    # Regular Expression with submission re.sub
    result = re.sub('["/*@&]', '', malist)

    print("Ma chaine aprés filter : ", result)

    print("*** Fin Exo 15 ***")
    print("\n")


str1 = "/*John est @developpeur & musicien "
exo15filtretring(str1)


###################
# EXO 16
def exo16filtretring(machaine) :
    """ Supprimer tous les caractères d’une chaine qui ne sont pas des entiers """
    print(" *** Début Exo 16 *** ")
    print(exo16filtretring.__doc__)
    print("Ma chaine avant : ", machaine)

    result=""
    # result = [int(char) for char in machaine.split() if char.isdigit()]
    result = re.sub("['a-zA-Z\s]|\'",'', machaine)  # through regular expression

    print("Ma chaine aprés filter : ", result)

    print("*** Fin Exo 16 ***")
    print("\n")


str1 = "J’ai 25 ans et 10 mois"
exo16filtretring(str1)


###################
# EXO 16
def exo17filtrealphanum(machaine) :
    """ Supprimer toutes  les caractères d’une chaine qui ne sont pas des entiers """
    print(" *** Début Exo 16 *** ")
    print(exo16filtretring.__doc__)
    print("Ma chaine avant : ", machaine)

    result=""
    # result = [int(char) for char in machaine.split() if char.isdigit()]
    result = re.sub("['a-zA-Z\s]|\'",'', machaine)  # through regular expression

    print("Ma chaine aprés filter : ", result)

    print("*** Fin Exo 16 ***")
    print("\n")


str1 = "J’ai 25 ans et 10 mois"
exo16filtretring(str1)



###################
# EXO 18
def exo18changebydieze(machaine) :
    """ Remplacer tous les signes de ponctuation d’une chaine par des # """
    print(" *** Début Exo 18 *** ")
    print(exo18changebydieze.__doc__)
    print("Ma chaine avant : ", machaine)

    result=""
    result = re.sub('\\"|\/|\*|\@|\&', '#', machaine)

    print("Ma chaine aprés filter : ", result)

    print("*** Fin Exo 18 ***")
    print("\n")


str1 = "Original : /*John est @developpeur & musicien !!"
exo18changebydieze(str1)