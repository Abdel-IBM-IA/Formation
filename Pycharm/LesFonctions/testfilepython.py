import numpy as np

print(sum(range(5), -1))
from numpy import *

print(sum(range(5), -1))
print("\n")

A24bis = np.random.randint(0, 100, (5, 3))
print(A24bis)
print("\n")
A24ter = np.random.randint(0, 100, (3, 2))
print(A24ter)
print("\n")
A24 = A24bis.dot(A24ter)
print(A24)

print((np.array(0) / np.array(0)))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))

Z = np.random.randint(0, 10, 4)
print("Z :")
print(Z)
print("\n")

print("Z ** Z")
print(Z ** Z)
print("\n")

print("2 << Z >> 2")
print(2 << Z >> 2)
print("\n")

print("Z < - Z")
print(Z < - Z)
print("\n")

print("1j * Z")
print(1j * Z)
print("\n")

print("Z / 1 / 1")
print(Z / 1 / 1)
print("\n")

print("Z < Z > Z")
print(Z < Z > Z)
print("\n")
