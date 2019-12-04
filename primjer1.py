import random
import numpy as np
import matplotlib.pyplot as plt
import WCut

# 500 tocaka, 5 klastera velicine redom 75, 130, 150, 70, 75
# Ovdje se mozda moze i random napravit klastere, samo je pitanje kako
# osigurat da su klasteri "ok" velicine a da i dalje ostane "random"

# tocke unutar klastera imaju bridove tezine izmedu [0, 1>, dok tocke izvan
# klastera imaju tezine izmedu [0, 0.1> za sum

velicine_klastera = [75, 130, 150, 70, 75]
A = np.zeros((500, 500))

for i in range(0, 500):
    tocke = 0
    klaster_i = 0
    while (i >= tocke):
        tocke = tocke + velicine_klastera[klaster_i]
        klaster_i = klaster_i + 1
    for j in range(i, 500):
        tocke = 0
        klaster_j = 0
        while (j >= tocke):
            tocke = tocke + velicine_klastera[klaster_j]
            klaster_j = klaster_j + 1
        if (klaster_i == klaster_j):
            A[i, j] = random.random()
            A[j, i] = random.random()

        else:
            A[i, j] = random.random() / 10
            A[j, i] = random.random() / 10

plt.matshow(A)
plt.colorbar()
plt.show()
