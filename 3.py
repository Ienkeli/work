import math
import matplotlib.pyplot as plt

# Практическая работа №3
# Вариант 7
# x*sin(x) - 1 = 0
# Преобразуем: x = 1/sin(x)

x0 = 1.1
eps = 1e-3
max_iter = 100

history = [x0]

for _ in range(max_iter):
    x1 = 1 / math.sin(x0)
    history.append(x1)

    if abs(x1 - x0) < eps:
        break

    x0 = x1

root = history[-1]

print("Практическая работа №3, вариант 7")
print("Метод простой итерации")
print("Уравнение: x*sin(x) - 1 = 0")
print(f"Корень: x = {root:.6f}")
print(f"f(x) = {root * math.sin(root) - 1:.6f}")

print("\nИтерации:")
for i, val in enumerate(history):
    print(f"{i:2d}: x = {val:.6f}")

# график сходимости
plt.figure(figsize=(8, 5))
plt.plot(range(len(history)), history, "o-", label="x_n")
plt.axhline(root, linestyle="--", label=f"корень ≈ {root:.4f}")
plt.xlabel("Номер итерации")
plt.ylabel("x")
plt.title("ПР3: сходимость метода итераций, вариант 7")
plt.legend()
plt.grid(True)
plt.savefig("pr3_variant7.png", dpi=150)
plt.close()