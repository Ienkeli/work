import math
import numpy as np
import matplotlib.pyplot as plt

# Практическая работа №4
# Вариант 7
# x*sin(x) - 1 = 0
# Методы хорд и касательных

eps = 1e-3

# Метод хорд/секущих
x0 = 1.1
x1 = 1.2
hord_hist = [x0, x1]

for _ in range(50):
    fx0 = x0 * math.sin(x0) - 1
    fx1 = x1 * math.sin(x1) - 1

    x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
    hord_hist.append(x2)

    if abs(x2 - x1) < eps:
        break

    x0, x1 = x1, x2

# Метод касательных Ньютона
x_newton = 1.2
newton_hist = [x_newton]

for _ in range(50):
    fx = x_newton * math.sin(x_newton) - 1
    dfx = math.sin(x_newton) + x_newton * math.cos(x_newton)

    x_next = x_newton - fx / dfx
    newton_hist.append(x_next)

    if abs(x_next - x_newton) < eps:
        break

    x_newton = x_next

print("Практическая работа №4, вариант 7")
print("Уравнение: x*sin(x) - 1 = 0\n")

print("Метод хорд:")
for i, val in enumerate(hord_hist):
    print(f"  Итерация {i}: x = {val:.6f}")
print(f"Корень методом хорд: x = {hord_hist[-1]:.6f}\n")

print("Метод касательных:")
for i, val in enumerate(newton_hist):
    print(f"  Итерация {i}: x = {val:.6f}")
print(f"Корень методом касательных: x = {newton_hist[-1]:.6f}")

# график функции
x = np.linspace(0.5, 2.0, 400)
y = x * np.sin(x) - 1

hord_root = hord_hist[-1]
newton_root = newton_hist[-1]

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="f(x)=x*sin(x)-1")
plt.axhline(0, color="black", linewidth=1)
plt.scatter(
    [hord_root],
    [hord_root * math.sin(hord_root) - 1],
    label="Метод хорд"
)
plt.scatter(
    [newton_root],
    [newton_root * math.sin(newton_root) - 1],
    label="Метод касательных"
)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("ПР4: корень уравнения, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr4_root_variant7.png", dpi=150)
plt.close()

# график сходимости
plt.figure(figsize=(8, 5))
plt.plot(range(len(hord_hist)), hord_hist, "o-", label="Метод хорд")
plt.plot(range(len(newton_hist)), newton_hist, "s-", label="Метод касательных")
plt.xlabel("Номер итерации")
plt.ylabel("x")
plt.title("ПР4: сходимость методов, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr4_convergence_variant7.png", dpi=150)
plt.close()
