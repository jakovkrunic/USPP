import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
from scipy.linalg import fractional_matrix_power
from sklearn.cluster import KMeans
import math

def Entropija(C):
    n = len(C)
    k = max(C)+1
    suma = 0
    for i in range(k):
        ni = C.count(i)
        p = ni/n
        suma +=p*math.log(p)
    return -1*suma

def Info(C1,C2):
    n = len(C1)     #broj tocaka oba klasteriranja mora biti isti
    k = max(C1)+1   #broj klastera oba klasteriranja mora biti isti
    suma = 0
    for i in range(k):
        for j in range(k):
            ni = C1.count(i)
            pi = ni/n
            nj = C2.count(j)
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

    
print(VI([1,1,0,2,2],[2,0,0,1,1]))


