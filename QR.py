import numpy as np
#
# A = np.array([[1.0, -2.0, 1.0],
#     [2.0, 0.0, -3.0],
#     [2.0, -1.0, -1.0]])
#
# B = [1.0,
#     8.0,
#     5.0]

A = np.array([
    [2.2, 4.0, -3.0, 1.5, 0.6, 2.0, 0.7],
    [4.0, 3.2, 1.5, -0.7, -0.8, 3.0, 1.0],
    [-3.0, 1.5, 1.8, 0.9, 3.0, 2.0, 2.0],
    [1.5, -0.7, 0.9, 2.2, 4.0, 3.0, 1.0],
    [0.6, -0.8, 3.0, 4.0, 3.2, 0.6, 0.7],
    [2.0, 3.0, 2.0, 3.0, 0.6, 2.2, 4.0],
    [0.7, 1.0, 2.0, 1.0, 0.7, 4.0, 3.2]])

B = [3.2,
    4.3,
    -0.1,
    3.5,
    5.3,
    9.0,
    3.7]

# A = np.array([
#     [2.0, -9.0, 5.0],
#     [1.2, -5.3999, 6.0],
#     [1.0, -1.0, -7.5]])
#
# B = [-4.0,
#     0.6001,
#     -8.5]

n = len(A)

A_copy = np.zeros((len(A), len(A[0]) + 1))
A_buf = np.zeros((len(A), len(A[0]) + 1))

A_copy = A.copy()

A_buf[:, : -1] = A
A_buf[:, n] = B


for i in range(n - 1):
    c = 0
    s = 0
    for j in range(i + 1, n):
        c = A_buf[i][i] / np.sqrt(A_buf[i][i]**2 + A_buf[j][i]**2)
        s = A_buf[j][i] / np.sqrt(A_buf[i][i]**2 + A_buf[j][i]**2)
        buffer_prev = A_buf[i, :] * c + A_buf[j, :] * s
        buffer_next = A_buf[i, :] * -s + A_buf[j, :] * c
        A_buf[i, :] = buffer_prev
        A_buf[j, :] = buffer_next

A = A_buf[:, : -1]
B = A_buf[:, n]

X = np.zeros(n)

X[n - 1] = B[n - 1] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    sumX = 0
    for j in range(i, n):
        sumX += A[i][j] * X[j]
    X[i] = (B[i] - sumX) / A[i][i]

print("X = ", X)

a = np.array([
    [8.0, -1.0, -2.0, 0.0],
    [0.0, 10.0, -2.0, 2.0],
    [-1.0, 0.0, 6.0, 2.0],
    [3.0, -1.0, 2.0, 12.0]
    ])

b = np.array([-2.3,
     0.5,
     1.2,
     -3.7])

result = np.linalg.solve(a, b)
print("program = ", result)

# a = np.array([[1.0, -2.0, 1.0],
#     [2.0, 0.0, -3.0],
#     [2.0, -1.0, -1.0]])
#
# b = np.array([1.0,
#     8.0,
#     5.0])
# result = np.linalg.solve(a, b)
# print("program = ", result)

Q = np.zeros(np.shape(A_buf))
R = np.zeros(np.shape(A_buf))

Q = np.dot(A_buf[:, : - 1], A_copy)
R = np.linalg.inv(A_buf[:, : - 1])

print(np.dot(R, Q))