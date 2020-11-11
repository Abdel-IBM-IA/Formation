# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'tools/')
import initialisation


selected = -1
tableau = []


def show_menu():
    print("\n" * 2)

    print(" 1. Trouver maximum dans la liste saisie de trois nombres")
    print(" 2. Afficher tous les nombres paires de 1 à n")
    print(" 3. Somme des entiers de 1 à n")
    print(" 4. Afficher la table de multiplication de n")
    print(" 5. Retrouver un Random en 10 étapes")
    print(" 6. Initialiser un tableau et identifier la valeur maxi")
    print(" 7. Initialiser un tableau et identifier le nombre de valeur pair et le nombre de valeur impaire")
    print(" 8. Multiple de 5 dans une liste de valeurs")
    print(" 9. Nombre de chiffre d'un nombre donné")
    print("10. Structure d'un nombre entier")
    print("11. Inverser les occurences d'une liste")
    print("12. 'OK' avec une boucle 'for'")

    selection = int(input("Faire votre choix :"))
    print("Votre choix : ", selection)
    return selection

bornemini=1
bornemaxi=12
options = {
    1: maxiOfOneListe,
    2: printEvenNumber,
    3: sumOfConsecutiveIntegers,
    4: displayMultiplicationTable,
    5: findNumberInTenSteps,
    6: findMaxValue,
    7: findHowManyEvenAndOddNumber,
    8: multipleOf5LessThan150,
    9: howManyDigitInNumber,
    10: pyramidalStructureOfAnInteger,
    11: reverseList,
    12: justPrintOK,
}


while selected < bornemini or selected > bornemaxi:
    selected = show_menu()
    if 0 < selected < 12:
        options[selected]()

    else:
        print("Merci de saisir une valeur comprise entre 1 et 12 !")





def saisiNombreEntier():
    nb = input("Veuillez saisir un entier :")
    while (type(nb) != int):
        nb = input("Merci de saisir un entier !")
    return nb


def maxiOfOneListe():
    print("maxiOfOneListe")


def maxiOfOneListe2():
    print("maxiOfOneListe")


def maxiOfOneListe3():
    print("maxiOfOneListe")


def maxiOfOneListe4():
    print("maxiOfOneListe")

def maxiOfOneListe5():
    print("maxiOfOneListe")


def maxiOfOneListe6():
    print("maxiOfOneListe")


def nbChiffreNbEntier():
    base=1
    cpt=0
    nbSaisi = saisiNombreEntier()
    while(base-nbSaisi<0):
        base = base * 10
        cpt=cpt+1
    print("Le nombre saisi est constitué de ", cpt-1, "chiffre(s)")


    print("maxiOfOneListe")