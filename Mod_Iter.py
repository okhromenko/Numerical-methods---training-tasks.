import numpy as np
import scipy

A = np.array([
    [10.0, 2.0, 1.0],
    [1.0, 10.0, 2.0],
    [1.0, 1.0, 10.0]])

b = np.array([
    10,
    12,
    8])

epsilon = 10 ** -3

n = len(A)

Y = np.zeros(n)
X = np.zeros(n)
T = np.zeros(n)


def norm(X):
    return np.max(X)

currentError = 1
countIter = 0

while(currentError >= epsilon):
    countIter += 1
    for i in range(len(A)):
        sum = 0
        for j in range(n):
            if(i != j):
                sum += Y[j] * A[i][j]
        X[i] = (b[i] - sum) / A[i][i]
        Y[i] = X[i]
    currentError = norm(np.abs(T - X))
    T = Y.copy()

print("X", X)
print("CountIter", countIter)
