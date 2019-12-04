import algvars
import primjer1
import CE
import VI
import numpy as np

def analyze_example(A,k,Cprime):
    vect = []
    vect.append( CE.All_renumberings(algvars.WNCut(A,k),Cprime) )
    vect.append( VI.VI(algvars.WNCut(A,k),Cprime) )

    vect.append( CE.All_renumberings(algvars.WACut(A,k),Cprime) )
    vect.append( VI.VI(algvars.WACut(A,k),Cprime) )

    vect.append( CE.All_renumberings(algvars.WNCutAplusAt(A,k),Cprime) )
    vect.append( VI.VI(algvars.WNCutAplusAt(A,k),Cprime) )

    vect.append( CE.All_renumberings(algvars.WACutAplusAt(A,k),Cprime) )
    vect.append( VI.VI(algvars.WACutAplusAt(A,k),Cprime) )

    vect.append( CE.All_renumberings(algvars.WNCutAAt(A,k),Cprime) )
    vect.append( VI.VI(algvars.WNCutAAt(A,k),Cprime) )

    vect.append( CE.All_renumberings(algvars.WACutAAt(A,k),Cprime) )
    vect.append( VI.VI(algvars.WACutAAt(A,k),Cprime) )

    return vect



if __name__ == "__main__":
    vect1 = np.zeros((20,12))
    for i in range(20):
        #75, 130, 150, 70, 75
        Cprime=np.zeros(500) + np.pad(np.ones(75),(425,0)) + np.pad(np.ones(145),(355,0)) + np.pad(np.ones(295),(205,0)) + np.pad(np.ones(425),(75,0))
        vect1[i] += analyze_example(primjer1.generiraj_1(),5,Cprime)
    for i in range(12):
        print (np.mean(vect1[:,i]))
        print ( np.var(vect1[:,i]) )
