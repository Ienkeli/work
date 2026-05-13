import math
import itertools
import numpy as np
import matplotlib.pyplot as plt

# Практическая работа №1
# Вариант 7
# Z = (a - sin(b)) / (b^2 + 6c)

a = 1.75
b = 1.21
c = 0.041

# границы абсолютных погрешностей по последнему разряду
da = 0.005
db = 0.005
dc = 0.0005


def z_value(a, b, c):
    return (a - math.sin(b)) / (b**2 + 6*c)


def z_value_np(a, b, c):
    return (a - np.sin(b)) / (b**2 + 6*c)


z = z_value(a, b, c)

# строгая оценка погрешности через частные производные
num = a - math.sin(b)
den = b**2 + 6*c

dz_da = 1 / den
dz_db = ((-math.cos(b)) * den - num * (2*b)) / den**2
dz_dc = -6 * num / den**2

delta_z = abs(dz_da)*da + abs(dz_db)*db + abs(dz_dc)*dc

# метод границ: перебираем все границы a, b, c
values = []
for aa, bb, cc in itertools.product([a-da, a+da], [b-db, b+db], [c-dc, c+dc]):
    values.append(z_value(aa, bb, cc))

z_low = min(values)
z_high = max(values)
z_mid = (z_low + z_high) / 2
z_half = (z_high - z_low) / 2

print("="*70)
print("Практическая работа №1, вариант 7")
print("="*70)
print(f"a = {a}, b = {b}, c = {c}")
print("Z = (a - sin(b)) / (b^2 + 6c)")
print(f"1. Значение Z: {z:.8f}")
print(f"2. Строгий учет погрешностей: Z = {z:.8f} ± {delta_z:.8f}")
print(f"3. Метод границ: {z_low:.8f} < Z < {z_high:.8f}")
print(f"   Z = {z_mid:.8f} ± {z_half:.8f}")

# график зависимости Z от b
b_grid = np.linspace(b - 0.08, b + 0.08, 300)
z_grid = z_value_np(a, b_grid, c)

plt.figure(figsize=(8, 5))
plt.plot(b_grid, z_grid, label="Z(b)")
plt.axvline(b, linestyle="--", label=f"b = {b}")
plt.axhline(z, linestyle=":", label=f"Z = {z:.5f}")
plt.xlabel("b")
plt.ylabel("Z")
plt.title("ПР1: вариант 7, зависимость Z от b")
plt.legend()
plt.grid(True)
plt.savefig("pr1_variant7.png", dpi=150)
plt.close()
