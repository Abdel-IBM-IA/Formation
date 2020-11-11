import numpy as np

a=np.array([[1,2,1,1],[0,1,2,1],[1,0,1,2],[2,1,0,1]])
print(np.linalg.det(a))
b=np.array([0,0,1,0])
x=np.linalg.solve(a,b)
print(x)
np.dot(a,x)