import numpy as np

a=np.random.rand(50,50)

b=a<=0.5

print("nombre de valeurs inferieures à 0.5 : ", np.sum(b))
a[a<=0.5]=0
a[a>0.5]=1
print(a)