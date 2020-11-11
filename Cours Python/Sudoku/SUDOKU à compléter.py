#-------------------------------------------------------------------------------
# Name:SUDOKU        module1
# Purpose: Controle grille remplie


A=[                         #initialisation matrice initiale conforme#
  [1,2,3,7,8,9,4,5,6],
  [4,5,6,1,2,3,7,8,9],
  [7,8,9,4,5,6,1,2,3],
  [3,1,2,9,7,8,6,4,5],
  [6,4,5,3,1,2,9,7,8],
  [9,7,8,6,4,5,3,1,2],
  [2,3,1,8,9,7,5,6,4],
  [5,6,4,2,3,1,8,9,7],
  [8,9,7,5,6,4,2,3,1]
  ]


E=[                         #initialisation matrice initiale non conforme#
  [1,2,7,3,8,9,4,5,6],
  [4,5,6,1,2,3,7,8,9],
  [3,8,9,4,5,6,1,2,3],
  [7,1,2,9,7,8,6,4,5],
  [6,4,5,3,1,2,9,7,8],
  [9,7,8,6,4,5,3,1,2],
  [2,3,1,8,9,7,5,6,4],
  [5,6,4,2,3,1,8,9,7],
  [8,9,7,5,6,4,2,3,1]
  ]


F=[                         #initialisation matrice initiale  non conforme#
  [1,1,11,7,8,9,4,5,6],
  [1,1,1,1,2,3,7,8,9],
  [1,1,1,4,5,6,1,2,3],
  [3,1,2,9,7,8,6,4,5],
  [6,4,5,3,1,2,9,7,8],
  [9,7,8,6,4,5,3,1,2],
  [2,3,1,8,9,7,5,6,4],
  [5,6,4,2,3,1,8,9,7],
  [8,9,7,5,6,4,2,3,1]
  ]


def affsudok(A):
    for i in range(9):              # permet un affichage de A ligne par ligne#
        print(A[i])


def sudotestline(A):        #Teste les lignes de la matrice
    lineok=True
    for i in range(9):
        testlin=1
        for j in range(9):
            testlin=testlin*A[i][j]
        if testlin!=362880:
            print('Il y a un probleme dans la ligne:',i)
            lineok=False
    if lineok:
        print("Pas de probleme sur les lignes")
    return lineok


def sudotestcarre(A):       #Teste les carre de la matrice
    carreok=True
    for k in range(9):
        testcarr=1
        i=(k//3)*3
        j=(k%3)*3
        for l in range(3):
            testcarr=testcarr*A[i+l][j]*A[i+l][j+1]*A[i+l][j+2]

        if testcarr!=362880:
            print('Il y a un probleme dans le carre:',k)        #les carres sont numerotes a artir de 0 par lignes de gauches a droite et de haut en bas
            carreok=False
    if carreok:
        print("Pas de probleme sur les carres")
    return carreok


def sudotestcol(A):        # A COMPLETER  TESTE LES COLONNES de la matrice
    colok=True
    for numligne in range (9):
        testcol=1
        for numcolonne in range (9):
            testcol=testcol*A[numligne][numcolonne]
        if testcol!=362880:
            print("Il ya un problème sur la colonne : ",numcolonne)
            colok=False
    if colok:
        print("Pas de pb sur les colonnes")
    return colok


def sudotestinterval(A):           # A COMPLETER On recherche des nombres non compris entre 1 et 9
    intervalok=True
    for numligne in range (9):
        for numcolonne in range (9):
            if A[numligne][numcolonne] < 0 or A[numligne][numcolonne] > 9:
                intervalok=False
                print("La valeur", A[numligne][numcolonne], "qui se trouve a la ligne :", numligne, " et la colonne :", numcolonne," n'est pas valide")
    if intervalok:
        print("Toutes les valeurs sont bien comprises entre 1 et 9")
    return intervalok


def sudotestglobal(A):
    print("*** Début Validation d'une grille de Sudoku ***")
    testInterval = sudotestinterval(A)
    testligne = sudotestline(A)
    testcolonne = sudotestcol(A)
    testcarre = sudotestcarre(A)
    if testInterval:
        if testligne and testcolonne and testcarre:
            print("La grille de soduko est validée !")
        else:
            print("La grille de soduko est erronée, la disposition logique des chiffres n'est pas respectée ! ")
    else:
        print("La grille de soduko est erronée, elle présente des valeurs inattendues !")
    print("*** Fin Validation de la validation de la grille de Sudoku ***")
    print("\n")


sudotestglobal(A)
sudotestglobal(E)
sudotestglobal(F)






