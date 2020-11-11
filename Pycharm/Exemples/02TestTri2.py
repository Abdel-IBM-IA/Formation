suite = [1,2,3,4,5]
N=len(suite)
resultat = True
i = 0
while i < N-1 :
    if suite[i] > suite[i+1] :
        resultat = False
        break
    i=i+1
print("le tableau est-il trié : ", resultat)