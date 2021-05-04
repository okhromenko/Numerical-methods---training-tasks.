import numpy as np


A = [
    [6.0, -1.0, -1.0, 1.0],
    [1.0, -2.0, 3.0, 1.0],
    [3.0, -4.0, -4.0, -1.0]]



# A = [
#     [2.0, -3.0, -4.0, 5.0, -13.0],
#     [4.0, -4.0, 1.0, -1.0, 14.0],
#     [6.0, -8.0, 3.0, 2.0, 15.0],
#     [2.0, 3.0, -2.0, 4.0, 7.0]]


# A = [
#     [5.0, 2.0, 3.0, 3.0],
#     [1.0, 6.0, 1.0, 5.0],
#     [3.0, -4.0, -2.0, 8.0]
# ]
#
# B = [
#     4.0,
#     2.0,
#     3.0
# ]


p = A[0][0]

for iter in range(len(A[0])):
    A[0][iter] = A[0][iter] / p

k = 1
i = 2
r = 1

def Value(k, r, iter):
    for i in range(iter, len(A[0])):
            sumZn = 0
            sumCh = 0
            for j in range(k):
                sumCh += A[j][i] * A[k][j]
                sumZn += A[j][k] * A[k][j]
            A[k][i] = (A[k][i] - (sumCh)) / (A[k][k] - (sumZn))

def Value_i(k, p, i):
    for iter in range(i, len(A[0])):
        for j in range(p - 1):
            A[j][iter] = A[j][iter] - A[k][iter] * A[j][k]

for j in range(len(A)):
    if j != len(A) - 1:
        Value(k, r, i)
    p = k + 1
    Value_i(k, p, i)
    k += 1
    i += 1

for i in range(len(A)):
    print("x", i, "=", A[i][len(A)])

a = np.array([
    [2.0, 2.0, 5.0, 7.0, 5.0, 2.0],
    [7.0, 98.0, 2.0, 4.0, 5.0, 4.0],
    [9.0, 18.0, 7.0, 17.0, 7.0, 24.0],
    [91.0, 8.0, 7.0, 78.0, 7.0, 4.0],
    [9.0, 81.0, 72.0, 27.0, 72.0, 74.0],
    [4.0, 7.0, 0.0, 51.0, 25.0, 55.0]])
b = np.array(
    [1.0,
     1.0,
     1.0,
    -5.0,
    -27.0,
    51.0])
result = np.linalg.solve(a, b)
print(result)



