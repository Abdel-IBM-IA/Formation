import numpy as np

from time import time

#1ere méthode avec une boucle
start=time()
sum=0
for i in range(1000001) :
    sum+=i
time1=time()-start


#2eme methode avec numpy
start=time()
a=np.sum(np.arange(1000001, dtype=np.int64))
time2=time()-start


rapport=time1/time2
print(rapport)
print(sum)
print(a)