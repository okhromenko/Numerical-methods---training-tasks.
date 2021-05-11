import numpy as np
import scipy

A = [
    [10.0, 2.0, 1.0],
    [1.0, 10.0, 2.0],
    [1.0, 1.0, 10.0]]

B = [10,
     12,
     8]

epsilon = 10 ** -6

def Max_X(X):
    return np.max(X)

X = np.zeros(len(A[0]))
X_pr = np.zeros(len(A[0]))


for i in range(len(A)):
    Zn = 0
    for j in range(len(A)):
        if (i != j):
            Zn -= A[i][j] * X_pr[j]
    X[i] = (B[i] + Zn) / A[i][i]

Bucket = np.zeros(len(A))
countIter = 1
currentError = 1


while Max_X(np.abs(X - X_pr)) >= epsilon:
    X_pr = X.copy()
    countIter += 1
    for i in range(len(A)):
        Zn = 0
        for j in range(len(A)):
            if (i != j):
                Zn -= A[i][j] * X_pr[j]
        Bucket[i] = (B[i] + Zn) / A[i][i]
    X = Bucket

print("X", X)
print("countIter", countIter)


