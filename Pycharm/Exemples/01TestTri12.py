suite = [1,2,3,6,5]
N=len(suite)
resultat = True
for i in range (0, N-1) :
    if suite[i] > suite[i+1] :
        resultat = False
        break
print ("le tableau est-il trié : ", resultat)