import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
from scipy.linalg import fractional_matrix_power
from sklearn.cluster import KMeans
import math

def Entropija(C):
    n = len(C)
    k = max(C.astype(int))+1
    suma = 0
    # Dacho nekaj peha
    unique, counts = np.unique(C, return_counts=True)
    dictC1=dict(zip(unique, counts))
    for i in range(k):
        ni = dictC1[i]
        p = ni/n
        suma +=p*math.log(p)
    return -1*suma

def Info(C1,C2):
    n = len(C1)     #broj tocaka oba klasteriranja mora biti isti
    k = max(C1.astype(int))+1   #broj klastera oba klasteriranja mora biti isti
    # Dacho nekaj peha
    unique, counts = np.unique(C1, return_counts=True)
    dictC1=dict(zip(unique, counts))
    unique, counts = np.unique(C2, return_counts=True)
    dictC2=dict(zip(unique, counts))
    suma = 0
    for i in range(k):
        for j in range(k):
            ni = dictC1[i]
            pi = ni/n
            nj = dictC2[j]
            pj = nj/n
            nij = 0
            for l in range(n):
                if(C1[l] == i and C2[l] == j):
                    nij+=1

            pij = nij/n
            if(pij>0):
                suma+=pij*math.log(pij/(pi*pj))

    return suma

def VI(C1,C2):
    return Entropija(C1)+Entropija(C2)-2*Info(C1,C2)


#print(VI([1,1,0,2,2],[2,0,0,1,1]))
#print (np.zeros(500)+np.pad(np.ones(75),(425,0))+np.pad(np.ones(145),(355,0))+np.pad(np.ones(295),(205,0))+np.pad(np.ones(425),(75,0)))
#print (np.pad(np.ones(75),(1,0) ) )
