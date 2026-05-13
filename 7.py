import numpy as np
import matplotlib.pyplot as plt

# Практическая работа №7
# Вариант 7
# В таблице ПР7 для варианта 7 указано: x0=-1, x1=1, x2=2, x3=4.

x_nodes_from_pdf = [-1, -1, 2, 4]
x_nodes = [-1, 1, 2, 4]  # исправленный вариант для вычислений
y_nodes = [4, 9, 1, 6]
x_val = 3.3


def lagrange_value(x_nodes, y_nodes, x_val):
    n = len(x_nodes)
    if len(set(x_nodes)) != n:
        raise ValueError("Узлы x должны быть различными.")
    result = 0.0

    for i in range(n):
        term = y_nodes[i]
        for j in range(n):
            if j != i:
                term *= (x_val - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term

    return result


def lagrange_poly(x_nodes, y_nodes):
    # возвращает коэффициенты полинома через numpy.poly1d
    p = np.poly1d([0.0])
    n = len(x_nodes)

    for i in range(n):
        li = np.poly1d([1.0])
        denom = 1.0

        for j in range(n):
            if i != j:
                li *= np.poly1d([1.0, -x_nodes[j]])
                denom *= x_nodes[i] - x_nodes[j]

        p += y_nodes[i] * li / denom

    return p


print("Практическая работа №7, вариант 7")
print("Интерполяционный многочлен Лагранжа")
print(f"Узлы из PDF: x = {x_nodes_from_pdf}")
print("В PDF есть повтор x=-1, поэтому расчет выполнен с исправлением x1=1.")
print(f"Использованные узлы: x = {x_nodes}, y = {y_nodes}")

p = lagrange_poly(x_nodes, y_nodes)
L = lagrange_value(x_nodes, y_nodes, x_val)

print("\nМногочлен Лагранжа:")
print(np.poly1d(np.round(p.coeffs, 6)))
print(f"\nL({x_val}) = {L:.6f}")

# график
x_dense = np.linspace(min(x_nodes) - 0.5, max(x_nodes) + 0.5, 300)
y_dense = p(x_dense)

plt.figure(figsize=(8, 5))
plt.plot(x_dense, y_dense, label="L(x)")
plt.plot(x_nodes, y_nodes, "ro", label="Узлы")
plt.plot(x_val, L, "gs", label=f"L({x_val})={L:.3f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("ПР7: многочлен Лагранжа, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr7_lagrange_variant7.png", dpi=150)
plt.close()
