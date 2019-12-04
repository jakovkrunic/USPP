import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
from scipy.linalg import fractional_matrix_power
from sklearn.cluster import KMeans

# zasad koristimo postojecu k-means funkciju, mozda kasnije napravimo svoju
# k je broj klastera

# 1. korak preskacemo i stavljamo da je T' = I (ako treba, lako se izmijeni)
# 2. korak


def stvoriD(A):
    x = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        suma = 0
        for j in range(A.shape[0]):
            suma += A[i, j]
        x[i] = suma
    return np.diag(x)
# 3. korak


def stvoriHB(A, T, D):
    t = fractional_matrix_power(T, -0.5)
    razlika = np.subtract(D*2, np.add(A, A.transpose()))
    temp = t * 0.5
    umnozak = np.matmul(temp, razlika)
    return np.matmul(umnozak, t)
# 4. korak


def stvoriY(HB, k):
    eigenValues, eigenVectors = la.eig(HB)
    idx = eigenValues.argsort()[:k][::1]
    eigenVectors = eigenVectors[:, idx]
    return eigenVectors


# 5. korak -- stvori X pa klasteriraj
def klasteriraj(T, Y, k):
    t = fractional_matrix_power(T, -0.5)
    X = np.matmul(t, Y)
    kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
    return kmeans.labels_  # isprinta vektor npr. [0,1,0]
    # prva i treca tocka pripadaju klasteru C0
    # druga tocka pripada klasteru C1


def WCut(A, T, k):
    D = stvoriD(A)
    HB = stvoriHB(A, T, D)
    Y = stvoriY(HB, k)
    return klasteriraj(T, Y, k)


# A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
# WCut(A,stvoriD(A),2) #ovdje stavljam da je T = D
