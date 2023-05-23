import sys
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

n, running, ld = 4, 100, 0.5

s = [[0 for _ in range(n)] for _ in range(n)]
s = [[8, 2, 8, 1], [7, 8, 7, 2], [1, 2, 9, 9], [4, 9, 8, 4]]
beta = [[0 for _ in range(n)] for _ in range(n)]
alpha = [[0 for _ in range(n)] for _ in range(n)]
raw = [[0 for _ in range(n)] for _ in range(n)]
etha = [[0 for _ in range(n)] for _ in range(n)]
connection = [0 for _ in range(n)]

while running > 0:
    running -= 1
    for i in range(n):
        for j in range(n):
            beta[i][j] = (s[i][j] + alpha[i][j]) * ld + beta[i][j] * (1 - ld)

    for i in range(n):
        for j in range(n):
            raw[i][j] = (s[i][j] + etha[i][j]) * ld + raw[i][j] * (1 - ld)

    for i in range(n):
        for j in range(n):
            maxi = -1000000
            for k in range(n):
                if k == j:
                    continue
                maxi = max(maxi, beta[i][k])
            etha[i][j] = -maxi * ld + etha[i][j] * (1 - ld)

    for i in range(n):
        for j in range(n):
            maxi = -1000000
            for k in range(n):
                if k == i:
                    continue
                maxi = max(maxi, raw[k][j])
            alpha[i][j] = -maxi * ld + alpha[i][j] * (1 - ld)

for i in range(n):
    for j in range(n):
        print(alpha[i][j] + raw[i][j], end=" ")
        if alpha[i][j] + raw[i][j] > 0:
            connection[i] = j
    print()

for i in range(n):
    print(i, connection[i])
