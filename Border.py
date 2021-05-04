import numpy as np

# S = [
#     [1.0, 1.0, 2.0, 3.0],
#     [0.0, 1.0, 1.0, -4.0],
#     [0.0, 0.0, 3.0, -27.0],
#     [0.0, 0.0, 0.0, 51.0]]
#
# B_x = [
#     [1.0,
#     -5.0,
#     -27.0,
#     51.0]]

S = [
    [2.0, 2.0, 5.0, 7.0, 5.0, 2.0],
    [7.0, 98.0, 2.0, 4.0, 5.0, 4.0],
    [9.0, 18.0, 7.0, 17.0, 7.0, 24.0],
    [91.0, 8.0, 7.0, 78.0, 7.0, 4.0],
    [9.0, 81.0, 72.0, 27.0, 72.0, 74.0],
    [4.0, 7.0, 0.0, 51.0, 25.0, 55.0]]

B_x = [
    [1.0,
     1.0,
     1.0,
    -5.0,
    -27.0,
    51.0]]

def Deconstruct(x_i, y_i, x_j, y_j):
    mas = np.zeros((n, n))
    i_0 = 0
    for i in range(x_i, y_i):
        j_0 = 0
        for j in range(x_j, y_j):
            mas[i_0][j_0] = S[i][j]
            j_0 += 1
        i_0 += 1
    return mas

def Join(S_1, X, x_i, y_i, x_j, y_j):
    i_0 = 0
    for i in range(x_i, y_i):
        j_0 = 0
        for j in range(x_j, y_j):
            S_1[i][j] = X[i_0][j_0]
            j_0 += 1
        i_0 += 1
    return S_1

n = int(len(S) / 2)

a = np.zeros((n, n))
b = np.zeros((n, n))
c = np.zeros((n, n))
d = np.zeros((n, n))

A = np.zeros((n, n))
B = np.zeros((n, n))
C = np.zeros((n, n))
D = np.zeros((n, n))


a = Deconstruct(0, n, 0, n)
b = Deconstruct(0, n, n, len(S))
c = Deconstruct(n, len(S), 0, n)
d = np.linalg.inv(Deconstruct(n, len(S), n, len(S)))


A = np.linalg.inv(a - np.dot(np.dot(b, d), c))
B = np.dot(np.dot(-A, b), d)
C = np.dot(np.dot(-d, c), A)
D = d - np.dot(np.dot(d, c), B)

S_1 = np.zeros((len(S), len(S)))

S_1 = Join(S_1, A, 0, n, 0, n)
S_1 = Join(S_1, B, 0, n, n, len(S))
S_1 = Join(S_1, C, n, len(S), 0, n)
S_1 = Join(S_1, D, n, len(S), n, len(S))


for i in range(len(S)):
    for j in range(len(S)):
        S_1[j][i] *= B_x[0][i]


X = np.zeros((len(S)))


for i in range(len(S)):
    for j in range(len(S)):
        X[i] += S_1[i][j]


print(X)



