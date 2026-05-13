import math
import numpy as np
import matplotlib.pyplot as plt

# Практическая работа №10
# Вариант 7
# yy' + x = 1, y(0.5)=0, [a;b]=[0.5;2.5], h=0.2


a = 0.5
b = 2.5
y0 = 0.0
h = 0.2


def f_ode(x, y):
    if abs(y) < 1e-12:
        raise ZeroDivisionError("При y=0 правая часть (1-x)/y не определена.")
    return (1 - x) / y


def exact_y(x):
    value = 2*x - x**2 - 0.75
    if value < 0:
        return float("nan")
    return math.sqrt(value)


x_values = np.arange(a, b + h/2, h)
y_exact = np.array([exact_y(float(x)) for x in x_values])

print("Практическая работа №10, вариант 7")
print("Уравнение: yy' + x = 1")
print("y' = (1-x)/y")
print(f"Начальное условие: y({a}) = {y0}")
print("\nОбычный метод Эйлера не стартует, потому что при y0=0 возникает деление на ноль.")
print("Точное решение: y^2 = 2x - x^2 - 0.75")
print("Вещественная ветвь существует только на [0.5; 1.5].\n")

print("Значения точного решения:")
for x, y in zip(x_values, y_exact):
    if np.isnan(y):
        print(f"x={x:.1f}, y не является вещественным")
    else:
        print(f"x={x:.1f}, y={y:.6f}")

# График точного решения
x_dense = np.linspace(a, b, 400)
y_dense = np.array([exact_y(float(x)) for x in x_dense])

plt.figure(figsize=(8, 5))
plt.plot(x_dense, y_dense, label="Точное решение, y>=0")
real_mask = ~np.isnan(y_exact)
plt.plot(x_values[real_mask], y_exact[real_mask], "ro", label="Точки с шагом h=0.2")
plt.axvline(1.5, linestyle="--", label="граница вещественного решения")
plt.xlabel("x")
plt.ylabel("y")
plt.title("ПР10: точное решение ОДУ, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr10_exact_variant7.png", dpi=150)
plt.close()
