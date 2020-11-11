import numpy as np

matrice=np.random.rand(50,50)

diff=matrice[:,1:]-matrice[:,:-1]

print(np.max(np.abs(diff)))
