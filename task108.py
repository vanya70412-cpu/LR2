v_kmh = float(input("Введіть швидкість у км/год (наприклад 60): "))
v_ms = float(input("Введіть швидкість у м/с (наприклад 16.7): "))

v_kmh_in_ms = v_kmh * 1000.0 / 3600.0

print(f"\nПеретворення швидкості: {v_kmh} км/год = {v_kmh_in_ms:.6f} м/с")
print(f"Задане значення: {v_ms:.6f} м/с")

if abs(v_kmh_in_ms - v_ms) < 1e-9:
    print("Обидві швидкості однакові після приведення до м/с")
elif v_kmh_in_ms > v_ms:
    print(f"Швидкість {v_kmh} км/год (≈{v_kmh_in_ms:.6f} м/с) більша")
else:
    print(f"Швидкість {v_ms:.6f} м/с більша")