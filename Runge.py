import math
import matplotlib.pyplot as plt


x = 0
y = 0

a = 0
b = 1
n = 10
h = (b - a) / n


def f(x, y):
    return 2*y - 2

def X_list(n, h):
    X_list = []
    x = 0
    for i in range(n + 1):
        X_list.append(x)
        x = x + h
    return X_list

def Exact_m(n, X_list_t):
    Y_decision = []
    for i in range(n + 1):
        func = 1 - math.e**(2*X_list_t[i])
        Y_decision.append(func)
    return Y_decision

def Polylines_m(h, n):
    #усовершенствованный метод ломаных
    X__list_Polylines = X_list(n, h)
    Y_list_Polylines = []
    Y_decision = Exact_m(n, X_list(n, h))
    y_Polylines = y
    for i in range(n + 1):
        Y_list_Polylines.append(y_Polylines)
        print(X__list_Polylines[i], " | ", y_Polylines, " | ", Y_decision[i], " | ", abs(Y_decision[i] - y_Polylines))
        k1 = f(X__list_Polylines[i], Y_list_Polylines[i])
        k2 = f(X__list_Polylines[i] + h/2, Y_list_Polylines[i] + h*k1/2)
        y_Polylines = y_Polylines + k2*h
    return X__list_Polylines, Y_list_Polylines


def Runge_K(h, n):
    #метод Рунге-Кутты 4-го порядка
    X__list_Runge_K = X_list(n, h)
    Y_list_Runge_K = []
    Y_decision = Exact_m(n, X_list(n, h))
    y_Runge_K = y
    for i in range(n + 1):
        Y_list_Runge_K.append(y_Runge_K)
        print(X__list_Runge_K[i], " | ", y_Runge_K, " | ", Y_decision[i], " | ", abs(Y_decision[i] - y_Runge_K))
        k1 = h * f(X__list_Runge_K[i], Y_list_Runge_K[i])
        k2 = h * f(X__list_Runge_K[i] + h / 2, Y_list_Runge_K[i] + k1 / 2)
        k3 = h * f(X__list_Runge_K[i] + h / 2, Y_list_Runge_K[i] + k2 / 2)
        k4 = h * f(X__list_Runge_K[i] + h, Y_list_Runge_K[i] + k3)
        y_Runge_K = y_Runge_K + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return X__list_Runge_K, Y_list_Runge_K



print("Усовершенствованный метод ломаных с шагом h =", h)
print("x | y | Точное решение | Погрешность")
X__list_Polylines, Y_list_Polylines = Polylines_m(h, n)
print("\nУсовершенствованный метод ломаных с шагом (h/2) =", h/2)
print("x | y | Точное решение | Погрешность")
X__list_Polylines_2, Y_list_Polylines_2 = Polylines_m(h/2, n*2)


print("\nМетод Рунге-Кутты 4-го порядка с шагом h =", h)
print("x | y | Точное решение | Погрешность")
X__list_Runge_K, Y_list_Runge_K = Runge_K(h, n)
print("\nМетод Рунге-Кутты 4-го порядка с шагом (h/2) =", h/2)
print("x | y | Точное решение | Погрешность")
X__list_Runge_K_2, Y_list_Runge_K_2 = Runge_K(h/2, n*2)

X_list_t = X_list(n, h)
Y_decision = Exact_m(n, X_list_t)


plt.plot(X_list_t, Y_decision, "o-", label="точное решение")
plt.plot(X__list_Runge_K, Y_list_Runge_K, "k-", label="метод Рунге-Кутты 4-го порядка")
plt.plot(X__list_Runge_K_2, Y_list_Runge_K_2, "r-", label="метод Рунге-Кутты 4-го порядка h/2")
plt.legend()
plt.grid()
plt.show()

plt.plot(X_list_t, Y_decision, "o-", label="точное решение")
plt.plot(X__list_Polylines, Y_list_Polylines, "k-", label="усовершенствованный метод ломаных")
plt.plot(X__list_Polylines_2, Y_list_Polylines_2, "r-", label="усовершенствованный метод ломаных h/2")
plt.legend()
plt.grid()
plt.show()