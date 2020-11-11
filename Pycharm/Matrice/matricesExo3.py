# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 09:51:57 2020

@author: user
"""


import numpy as np

#colonne de 1 sur 7 lignes
col_uns=np.ones((7,1))

#Concatenation à droite et à gauche des colonnes à une matrice nulle (7x6)
a=np.concatenate((col_uns,np.zeros((7,6)),col_uns),axis=1)
print(a)
final=np.concatenate((a,np.ones((1,8))))

print(final)