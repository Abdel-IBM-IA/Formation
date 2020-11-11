import numpy as np

def est_triangulaire_sup(M) :
    n,p = np.shape(M)
    if n != p :
        return False
    else :
        for i in range(n) :
            for j in range(i) : 
                if M[i,j] == 0 :
                    return True
                else : 
                    return False

    
def est_triangulaire_sup2(M):
    return(M == np.triu(M)).all()

def est_diagonale(M) :
    n,p = np.shape(M)
    print(n,p)
    if n != p :
        return False
    for i in range(n) :
        for j in range(p) :
            if i != j and M[i,j] != 0 :
                return False
 
    return True
    
def est_diagonale2(M) : 
    return(M==np.triu(np.tril(M))).all()

if __name__ == '__main__':
    print_hi('PyCharm')
    A= np.array([3,0,0],[0,8,0],[0,0,12])
    est_diagonale2(A)
