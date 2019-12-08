import algvars
import primjer1
import primjer2
import CE
import VI
import numpy as np


def analyze_example(A, k, Cprime):
    vect = []
    vect.append(CE.Hungarian(algvars.WNCut(A, k), Cprime))
    vect.append(VI.VI(algvars.WNCut(A, k), Cprime))

    vect.append(CE.Hungarian(algvars.WACut(A, k), Cprime))
    vect.append(VI.VI(algvars.WACut(A, k), Cprime))

    vect.append(CE.Hungarian(algvars.WNCutAplusAt(A, k), Cprime))
    vect.append(VI.VI(algvars.WNCutAplusAt(A, k), Cprime))

    vect.append(CE.Hungarian(algvars.WACutAplusAt(A, k), Cprime))
    vect.append(VI.VI(algvars.WACutAplusAt(A, k), Cprime))

    vect.append(CE.Hungarian(algvars.WNCutAAt(A, k), Cprime))
    vect.append(VI.VI(algvars.WNCutAAt(A, k), Cprime))

    vect.append(CE.Hungarian(algvars.WACutAAt(A, k), Cprime))
    vect.append(VI.VI(algvars.WACutAAt(A, k), Cprime))

    return vect


def print_means_vars(vect, dim):
    for i in range(dim):
        print(np.mean(vect[:, i]))
        print(np.var(vect[:, i]))
    print()


def generate_examples(Cprime, no_of_clusters, generate_affinity_matrix):
    vect = np.zeros((20, 12))
    for i in range(20):
        vect[i] += analyze_example(generate_affinity_matrix(),
                                   no_of_clusters,
                                   Cprime)
    print_means_vars(vect, 12)


if __name__ == "__main__":
    # 75, 130, 150, 70, 75
    Cprime = (np.pad(np.ones(75), (425, 0)) +
              np.pad(np.ones(145), (355, 0)) +
              np.pad(np.ones(295), (205, 0)) +
              np.pad(np.ones(425), (75, 0)))
    generate_examples(Cprime, 5, primjer1.generiraj_1)
    # 100,100,100,100
    Cprime = (np.pad(np.ones(100), (300, 0)) +
              np.pad(np.ones(200), (200, 0)) +
              np.pad(np.ones(300), (100, 0)))
    generate_examples(Cprime, 4, primjer2.generiraj_2)
