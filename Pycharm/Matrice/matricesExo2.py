import numpy as np

#Avec boucle
def est_triangulaire_sup(M):
    n, p = np.shape(M)
    flag = False
    if n != p:
        return False
    else:
        for i in range(n):
            for j in range(i):
                if M[i, j] == 0:
                    flag =  True
    return flag

#En une ligne
def est_triangulaire_sup2(M):
    return (M == np.triu(M)).all()


def est_diagonale(M):
    n, p = np.shape(M)
    if n != p:
        return False
    for i in range(n):
        for j in range(p):
            if i != j and M[i, j] != 0:
                return False


#En une ligne
def est_diagonale2(M):
    return (M == np.triu(np.tril(M))).all()


A = np.array([[3, 1, 0], [0, 8, 0], [0, 0, 12]])
print(A)
print(est_diagonale(A))
print(est_diagonale2(A))
print(est_triangulaire_sup2(A))
print(est_triangulaire_sup(A))

