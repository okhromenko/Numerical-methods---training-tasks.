import numpy as np

# A = [
#     [2.0, -3.0, -4.0, 5.0],
#     [4.0, -4.0, 1.0, -1.0],
#     [6.0, -8.0, 3.0, 2.0],
#     [2.0, 3.0, -2.0, 4.0]]
#
# B = [
#     [-13.0,
#     14.0,
#     15.0,
#     7.0]]

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

A = [
    [1.0, 1.0, 2.0, 3.0],
    [0.0, 1.0, 1.0, -4.0],
    [0.0, 0.0, 3.0, -27.0],
    [0.0, 0.0, 0.0, 51.0]]

B = [
    [1.0,
    -5.0,
    -27.0,
    51.0]]

U = np.zeros((len(A), len(A[0])))
L = np.zeros((len(A), len(A[0])))

for i in range(len(A[0])):
    U[0][i] = A[0][i]

for i in range(len(A)):
    L[i][i] = 1
    L[i][0] = A[i][0] / U[0][0]


for i in range(len(A)):
    for j in range(i, len(A)):
        sumU = 0
        for k in range(i):
            sumU += L[i][k] * U[k][j]
        U[i][j] = A[i][j] - sumU

        sumL = 0
        for k in range(i):
            sumL += L[j][k] * U[k][i]
        L[j][i] = (A[j][i] - sumL) / U[i][i]

# P, Lp, Up = lu(A)
# print(Lp)

Y = np.zeros((len(A)))
Y[0] = B[0][0]


n = len(A)
for i in range(n):
        sumY = 0
        for j in range(i):
            sumY += L[i][j] * Y[j]
        Y[i] = B[0][i] - sumY

X = np.zeros(n)
X[0] = Y[n - 1] / U[n - 1][n - 1]

for i in range(1, n + 1):
    sumX = 0
    for j in range(1, i):
        sumX += U[n - i][n - j] * X[n - j]
    X[n - i] = (Y[n - i] - sumX) / U[n - i][n - i]

print(X)

