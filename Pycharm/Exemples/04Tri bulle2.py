# Liste=[9,8,7,2,6,5]
Liste = ['A', 'B', 'z', 'G', 'Z', 'H', 'O', 'P']
print(Liste)


def permutation(L, i, j):
    if (L != None):
        if (i < len(L) and j < len(L)):
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
        else:
            print("les bornes sont incorrectes")
    else:
        print("La liste n'existe pas")


def compare_permute(L, i):
    if (L != None):
        if ((i + 1) < len(L)):
            if (L[i] > L[i + 1]):
                permutation(L, i, (i + 1))
        else:
            print("les bornes sont incorrectes")
    else:
        print("La liste n'existe pas")


def many_compare_permute(L):
    if (L != None):
        n = len(L)
        for i in range(0, n - 1):
            compare_permute(L, i)
    else:
        print("La liste n'existe pas")


def tri_bulle(L):
    if (L != None):
        n = len(L)
        i = 0
        while i < (n - 1):
            if (L[i] > L[i + 1]):
                many_compare_permute(L)
                i = 0
            i += 1
    else:
        print("La liste n'existe pas")


tri_bulle(Liste)
print(Liste)