import cmath
import numpy as np


# A = [
#     [6.0, -1.0, -1.0],
#     [1.0, -2.0, 3.0],
#     [3.0, -4.0, -4.0]]
#
# B = [
#     [1.0,
#     1.0,
#     -1.0]]


# A = [
#     [1.0, 2.0, 4.0],
#     [2.0, 13.0, 23.0],
#     [4.0, 23.0, 77.0]]
#
# B = [
#     [10.0,
#     50.0,
#     150.0]]

A = [
    [2.2, 4.0, -3.0, 1.5, 0.6, 2.0, 0.7],
    [4.0, 3.2, 1.5, -0.7, -0.8, 3.0, 1.0],
    [-3.0, 1.5, 1.8, 0.9, 3.0, 2.0, 2.0],
    [1.5, -0.7, 0.9, 2.2, 4.0, 3.0, 1.0],
    [0.6, -0.8, 3.0, 4.0, 3.2, 0.6, 0.7],
    [2.0, 3.0, 2.0, 3.0, 0.6, 2.2, 4.0],
    [0.7, 1.0, 2.0, 1.0, 0.7, 4.0, 3.2]]

B = [
    [3.2,
    4.3,
    -0.1,
    3.5,
    5.3,
    9.0,
    3.7]]


# A = [
#     [1.0, 3.0, -2.0, 0.0, -2.0],
#     [3.0, 4.0, -5.0, 1.0, -3.0],
#     [-2.0, -5.0, 3.0, -2.0, 2.0],
#     [0.0, 1.0, -2.0, 5.0, 3.0],
#     [-2.0, -3.0, 2.0, 3.0, 4.0]]
#
# B = [
#     [0.5,
#     5.4,
#     5.0,
#     7.5,
#     3.3]]

n = len(A[0])

S = np.zeros((n, n), dtype=complex)

S[0][0] = cmath.sqrt(A[0][0])

for i in range(1, n):
    S[0][i] = A[0][i] / S[0][0]

for i in range(1, n):
    sumU = 0
    for j in range(i):
        sumU += (S[j][i])**2
    S[i][i] = cmath.sqrt(A[i][i] - sumU)
    if i > 0:
        for j in range(n):
            if i < j:
                sumL = 0
                for k in range(i):
                    sumL += S[k][i] * S[k][j]
                S[i][j] = (A[i][j] - sumL) / S[i][i]
            if i > j:
                S[i][j] = 0


Y = np.zeros(n, dtype = complex)
X = np.zeros(n, dtype = complex)

Y[0] = B[0][0] / S[0][0]


for i in range(1, n):
    sumY = 0
    for j in range(i):
        sumY += S[j][i] * Y[j]
    Y[i] = (B[0][i] - sumY) / S[i][i]


X[n - 1] = Y[n - 1] / S[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    sumX = 0
    for j in range(i, n):
        sumX += S[i][j] * X[j]
    X[i] = (Y[i] - sumX) / S[i][i]
print(X)