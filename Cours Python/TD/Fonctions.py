#!/usr/bin/env python
# coding: utf-8

# # Fonctions en python

# ## Exercice 1 : Comparer deux nombres
# 
# Écrire la fonction compare() qui reçoit deux valeurs en argument a et b et affiche un message adapté selon que a est supérieur, inférieur ou égal à à b. Faire des essais en utilisant des entiers, des flottants et des chaînes de caractères. 

# In[ ]:


import unicodedata


def oterlesaccents(ch) :
    """Supprime les accents sans changer la casse (majuscules et minuscules)"""
    r = u""
    for car in ch :
        if car == u"\xA0" : # Pour conserver les espaces (espaces insécables également)
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
        elif a==b:
            result = "La valeur de la chaine de caractère(s) des deux arguments passés est identique : \"" + a + "\""
        else :
            result = "La valeur de la chaine de caractère(s) des deux arguments passés est équivalente : \"" + a +"\" et \"" + b +"\""

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
        result = "Les deux paramètres ne sont pas de même nature, et ne sont pas comparables \ntype a :" + str(type(a)) + "\ntype b :" + str(type(b))

    return result


# ## Exercice 2 : Test de parité 

# ### Question 2.1 :
# 
# Écrire la fonction estPair() qui affiche si un nombre reçu en paramètre est pair ou non. Faire des essais en utilisant des entiers, des flottants et des chaînes de caractères. Prévoir les résultats. 
# 

# In[2]:


def estPair(nb) :
    if isinstance(nb, (int, float)) :
        if (nb % 2) == 0 :
            print(str(nb) + " est un nombre pair")
        else :
            print(str(nb) + " est un nombre impair")
    elif nb is None :
        print("La valeur à tester est nulle !")
    else :
        print("La valeur saisie n'est pas un nombre :", nb)


nb = 4
estPair(nb)

nb = 5
estPair(nb)

nb = 2.0
estPair(nb)

nb = 5.0
estPair(nb)

nb = 'e'
estPair(nb)

nb = "azer"
estPair(nb)

estPair(None)


# ### Question 2.2 : 
# 
# Ré-écrire la fonction estPair() pour que cette dernière renvoie True si le nombre reçu en paramètre est pair, False sinon. Faire des essais en utilisant des entiers, des flottants et avec des chaînes de caractères. Prévoir les résultats. 

# In[8]:


def estPair(nb) :

    if isinstance(nb, (int, float)) :
        result = ((nb % 2) == 0)
        print(str(nb) + " est un nombre paire : " + str(result))
    else :
        result = False
        print(str(nb) + " est un nombre paire : " + str(result))
    return result


nb = 4
estPair(nb)

nb = 5
estPair(nb)

nb = 2.0
estPair(nb)

nb = 5.0
estPair(nb)

nb = 'e'
estPair(nb)

nb = "azer"
estPair(nb)

estPair(None)


# ## Exercice 3 : Moyenne de deux nombres
# 
# Écrire la fonction qui reçoit deux nombres en arguments et qui calcule et renvoie leur moyenne. Quel est le problème si les deux nombres sont entiers? Quelle solution proposez-vous? 

# In[3]:


def moyennede2(*args) :
    print("\n")
    if len(args) == 2 :
        print(args[0])
        print(args[1])
        if isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)) :
            result = (float(args[0]) + float(nb2)) / 2
            print("La moyenne de " + str(args[0]) + " et " + str(args[1]) + " est : " + str(result))
            return result
        else :
            if isinstance(args[0], str) :
                if isinstance(args[1], str) :
                    print("Les deux paramètres ne sont pas numériques")
                elif isinstance(args[1], type(None)) :
                    print("Le premier paramètre n'est pas numérique et le second est null")
                else :
                    print("Le premier paramètre n'est pas numérique")
            elif isinstance(args[0], type(None)) :
                if isinstance(args[1], type(None)) :
                    print("Les deux paramètres sont null")
                elif isinstance(args[1], str):
                    print("Le premier paramètre est null et le second n'est pas numérique")
                else :
                    print("Le premier paramètre est null")
            else :
                if isinstance(args[1], type(None)) :
                    print("Le second paramètre est null")
                elif isinstance(args[1], str) :
                    print("Le second paramètre n'est pas numérique")
    else :
        print("2 arguments attendus, nombre argument(s) reçu(s) : ", len(args))


nb1 = 4
nb2 = 5
moyennede2(nb1, nb2)

nb1 = 2.0
nb2 = 5
moyennede2(nb1, nb2)

nb1 = 2.0
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = None
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = None
nb2 = None
moyennede2(nb1, nb2)

nb1 = 'e'
nb2 = 5.0
moyennede2(nb1, nb2)

nb1 = 'e'
nb2 = "azer"
moyennede2(nb1, nb2)

nb1 = 2.0
moyennede2(nb1)


# ## Exercice 4 : Année bissextile 
# Écrire une fonction qui permet de déterminer si une année est bissextile. 
# 
# On rappelle qu’une année est bissextile si 
# elle est divisible par 4 
# mais n’est pas divisible par 100 
# sauf si elle est divisible par 400
# Ainsi 2008 était bissextile, 1900 n’était pas bissextile et 2000 était bissextile. 
# 
# 

# In[1]:


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


# ## Exercice 5 : Lancer de dés 
# 
# Le but de cet exercice est de créer des fonctions permettant de simuler des lancers de dés. 
# Lancer un dé correspond, d’un point de vue informatique, à tirer un entier aléatoire entre 1 et 6 inclus. Ceci se fait à l’aide de la fonction randint() contenue dans la bibliothèque random. Le code suivant permet de simuler le lancer d’un dé et d’afficher le résultat du lancer. 
# ```
# #nécessaire pour pouvoir utiliser la fonction randint()
# from random import * 
# de = randint(1,6) 
# print(’lancer : ’ + str(de))
# ```

# ### Question 5.1 : 
# 
# Créer une fonction qui simule le lancer de deux dés et renvoie la somme. Utiliser cette fonction pour afficher le résultat d’un lancer de deux dés. 
# 
# 

# In[ ]:


from random import *


def jet2De() :
    de = randint(1, 6)
    print("lancer: " + str(de))


jet2De()


# ### Question 5.2 : 
# 
# Créer une fonction qui simule le lancer d’un nombre quelconque de dés donné en paramètre. Utiliser cette fonction pour afficher le résultat d’un lancer de deux dés puis de trois dés.

# In[ ]:


def jetNDe(nb) :
    if isinstance(nb, int) : 
        for cpt in range(nb) : 
            de = randint(1, 6)
            print("lancer " + str(cpt + 1) + ": " + str(de))
        print("\n")
    else : 
        print("La saisie est erronnée, veuillez saisir un nombre entier pour le nombre de lancer de dé(s) :")


print("jet de 2 dés")
jetNDe(2)
print("jet de 3 dés")
jetNDe(3)


# ## Exercice 6 : Suite de carrés 
# 
# Écrire une fonction qui permet d’afficher la suite des carrés jusqu’à n2 où n est un entier choisi par l’utilisateur. 
# 
# L’affichage se fera sous la forme 
# 0 − 1 − 4 − 9 − 16 − 25 − 36 − 49 − 64 − 81 − 100...
# 
# Dans l’exemple suivant l’entier n est égal à 6 : 0−1−4−9−16−25−36. 

# In[4]:


def listeNCarre(nb) :
    if isinstance(nb, int) :
        result = ""
        for cpt in range(nb) :
            result += str(cpt*cpt) + " - "
        result = result[:-3] # Supprime les trois derniers caractères
        print(result) 
    else :
        print("La saisie est erronnée, veuillez saisir un nombre entier pour le nombre :")


listeNCarre(11)


# ## Exercice 7 : Produit d’entiers 
# 
# Écrire une fonction produit() qui calcule et renvoie le produit n1∗(n1+1)∗...∗n2 (tels que 1<=n1<= n2) des entiers compris entre n1 et n2 inclus. 

# In[6]:


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


# ## Exercice 8 : Échange de variables
# 
# Écrire une fonction swap(u,v) qui sert à échanger les valeurs de 2 variables u et v passées en arguments. 
# 
# Cette fonction est-elle utile? 
# 
# À quels types s’applique-t-elle? 

# In[ ]:


from copy import copy


def swap(var1, var2):
    """ Permet d'échanger les valeurs de 2 variables passées en arguments
    Les deux variables doivent être de même type"""
    return copy(var2), copy(var1)

# Fonction moyennement utile
# Elle s'applique uniquement au entier et float => les deux variables doivent être de même type 


# ## Exercice 9 : Comptage des éléments d’un tableau
# Écrire une fonction nbPairImpair() qui renvoie le nombre d’élément(s) pair(s) et le nombre d’élément(s) impair(s) dans le tableau reçu en argument. 

# In[1]:


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


# ## Exercice 10 : Décalage des éléments d’un tableau à droite
# Écrire une fonction decaleCircDroite() qui réalise le décalage circulaire vers la droite d’un tableau d’entiers. 
# Voici un exemple d’utilisation de cette fonction : 
# - Avant décalage circulaire a droite [12, 21, 10, 11, 0, 1, 6, 8]
# - Après décalage circulaire a droite [8, 12, 21, 10, 11, 0, 1, 6] 

# In[ ]:


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


# ## Exercice 11 : Rappel sur binaire

# ### Question 11.1 : Du binaire vers le décimal. 
# Écrire une fonction bin2Dec() qui permet de convertir une chaîne de caractères contenant la représentation binaire d’un nombre (codage entier naturel) en sa représentation décimale. 
# 
# Exemple d’utilisation : 
# ```
# nBin='10000001' 
# nDec = bin2Dec(nBin) 
# print('Le nombre binaire',nBin, 'se convertit en base 10 :', nDec)
# ```

# In[ ]:


def bin2Dec(nbBinaire):
    binaryCheck = re.compile('[0-1]')
    if not isinstance('str', type(nbBinaire)):
        nbBinaire = str(nbBinaire)
    if nbBinaire[0:2] != '0b':
        nbBinaire = '0b' + nbBinaire
    if binaryCheck.match(nbBinaire[2:]):
        return int(nbBinaire, 2)
    else:
        NotImplemented


# ### Question 12.2 : Du décimal vers le binaire. 
# Écrire une fonction qui calcule l’écriture en base 2 d’un nombre entier positif passé en argument sous sa forme décimale. Le résultat pour 5 sera 101.

# In[ ]:


def dec2Bin2(nbDecimal):
    return format(nbDecimal, '064b')


nDecimal = 9
dec2Bin(nDecimal)
print('Le nombre ', nDecimal, 'se convertit en binaire en :', dec2Bin(nDecimal))

