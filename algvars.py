import WCut
import numpy as np

def WNCut(A,k):
    return WCut.WCut(A,WCut.stvoriD(A),k)

def WACut(A,k):
    return WCut.WCut(A,np.identity(A.shape[0]),k)

def WNCutAplusAt(A,k):
    return WNCut(A+np.transpose(A),k)

def WACutAplusAt(A,k):
    return WACut(A+np.transpose(A),k)

def WNCutAAt(A,k):
    return WNCut(np.matmul(A,np.transpose(A)),k)

def WACutAAt(A,k):
    return WACut(np.matmul(A,np.transpose(A)),k)
