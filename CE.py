import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
from scipy.linalg import fractional_matrix_power
from sklearn.cluster import KMeans
import math


def CE(C1,C2):
    n = len(C1)     #broj tocaka oba klasteriranja mora biti isti
    k = max(C1)+1   #broj klastera oba klasteriranja mora biti isti
    suma = 0
    for i in range(k):
        for j in range(k):
            if(j != i):
                nij = 0
                for l in range(n):
                    if(C1[l] == i and C2[l] == j):
                        nij+=1
                suma+=nij
                
            
    return suma/n
        
print(CE([1,1,0,2,2],[2,0,0,1,1]))
print(CE([0,1,0],[0,1,0]))
