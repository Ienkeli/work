import math
import numpy as np
import matplotlib.pyplot as plt

# Практическая работа №2
# Вариант 7
# x*sin(x) - 1 = 0
# Метод половинного деления

def f(x):
    return x * math.sin(x) - 1


a = 1.1
b = 1.2
eps = 1e-3

if f(a) * f(b) > 0:
    raise ValueError("На выбранном отрезке нет смены знака.")

history = []
while (b - a) / 2 > eps:
    c = (a + b) / 2
    history.append((a, b, c, f(c)))
    if f(a) * f(c) <= 0:
        b = c
    else:
        a = c

root = (a + b) / 2

print("Практическая работа №2, вариант 7")
print("Метод половинного деления")
print("Уравнение: x*sin(x) - 1 = 0")
print(f"Корень: x = {root:.6f}")
print(f"Значение функции: f(x) = {f(root):.6f}")
print(f"Погрешность: ±{(b-a)/2:.6f}")
print("\nИтерации:")
for i, row in enumerate(history, start=1):
    aa, bb, cc, fc = row
    print(f"{i:2d}: a={aa:.6f}, b={bb:.6f}, c={cc:.6f}, f(c)={fc:.6f}")

# график функции
x = np.linspace(0.5, 2.0, 400)
y = x * np.sin(x) - 1

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="f(x)=x*sin(x)-1")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(root, linestyle="--", label=f"x ≈ {root:.4f}")
plt.scatter([root], [f(root)], zorder=5)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("ПР2: метод половинного деления, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr2_variant7.png", dpi=150)
plt.close()
