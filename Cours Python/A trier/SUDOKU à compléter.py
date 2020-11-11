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
            print('Il y a un probleme dans le carre:',k)        #les carres sont numerotes ÃƒÂ  partir de 0 par lignes de gauches ÃƒÂ  droite et de haut en bas
            carreok=False
    if carreok:
        print("Pas de probleme sur les carres")
    return carreok





def sudotestcol(A):        # A COMPLETER  TESTE LES COLONNES de la matrice
    colok=True
    for m in range (9):
        testcol=1
        for n in range (9):
            testcol=testcol*A[m][n]
        if testcol!=362880:
            print("la colonne",m,"comporte un probleme" )
            colok=False
    if colok:
        print("Pas de pb sur les colonnes")
    return colok

   



def sudotestinterval(A):           # A COMPLETER   On recherche des nombres non compris entre 1 et 9
    intervalok=True
    for o in range (9):
        for p in range (9):
            if A[o][p] < 0 or A[o][p] > 9 or type(A[o][p])!= int :
                intervalok=False
                print(A[o][p], "qui se trouve a la ligne",o,"et la colonne",p," n'est pas un chiffre valide")
    if intervalok:
        print("Les valeurs sont bien comprises entre 1 et 9")
    return intervalok
                
def sudotestfinal(A):
    lineok = sudotestline(A)
    carreok = sudotestcarre(A)
    colok = sudotestcol(A)
    intervalok = sudotestinterval(A)
    if lineok and carreok and colok and intervalok:
        print("La grille est juste")
        
    else:
        print("La grille est fausse")
        
sudotestfinal(A)
sudotestfinal(E)
sudotestfinal(F)






