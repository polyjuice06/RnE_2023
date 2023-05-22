import matplotlib.pyplot as plt
import numpy as np

n = 17
minus_inf = -213456789
inf = 213456789
ld = 0.5

s = [[i for i in range(n)] for _ in range(n)]
a = [[0 for _ in range(n)] for _ in range(n)]
r = [[0 for _ in range(n)] for _ in range(n)]
points = [
    [0, 0, -100],
    [10, 2, -100],
    [3, 6, -100],
    [4, 8, -100],
    [100, 140, -100],
    [120, 100, -100],
    [110, 120, -100],
    [0, 120, -100],
    [2, 110, -100],
    [1, 120, -100],
    [5, 120, -100],
    [20, 50, -100],
    [40, 100, -100],
    [60, 120, -100],
    [110, 20, -100],
    [80, 40, -100],
    [90, 35, -100],
]

exemplars, exemplar1s = [-1 for _ in range(n)], [inf for _ in range(n)]
running = 0


for i in range(n):
    for j in range(n):
        if i == j:
            s[i][j] = points[i][2]
        else:
            s[i][j] = -((points[i][1] - points[j][1]) ** 2) - (
                (points[i][0] - points[j][0]) ** 2
            )

while running < 10:
    for i in range(n):
        for j in range(n):
            maxi = minus_inf
            for k in range(n):
                if k == j:
                    continue
                maxi = max(maxi, a[i][k] + s[i][k])
            r[i][j] = (s[i][j] - maxi) * ld + r[i][j] * (1 - ld)
    for i in range(n):
        check = 0
        for j in range(n):
            if i == j:
                continue
            check += max(0, r[j][i])
        a[i][i] = check * ld + a[i][i] * (1 - ld)
    for i in range(n):
        for j in range(n):
            ret = 0
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                ret += max(0, r[k][j])
            a[i][j] = min(0, r[j][j] * ld + ret * ld) + a[i][j] * (1 - ld)
    for i in range(n):
        cur_exemplar, cur_value = i, minus_inf
        for j in range(n):
            if a[i][j] + r[i][j] > cur_value:
                cur_exemplar = j
                cur_value = a[i][j] + r[i][j]
        exemplars[i] = cur_exemplar
    running += 1
    for i in range(n):
        if exemplars[i] != exemplar1s[i]:
            running = 0
            break
    for i in range(n):
        exemplar1s[i] = exemplars[i]

for i in range(len(exemplars)):
    print(i, exemplars[i])

setofexe = list(set(exemplars))

for i in range(len(setofexe)):
    x, y = [], []
    for j in range(len(exemplars)):
        if exemplars[j] == setofexe[i]:
            x.append(points[j][0])
            y.append(points[j][1])
    plt.scatter(x, y)
plt.show()
