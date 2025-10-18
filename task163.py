import math

area = 0.0 
PI = 3.14

shape = input("Введіть тип кімнати (triangle/rectangle/circle): ").strip().lower()

if shape == "triangle":
    a = float(input("Введіть першу сторону трикутника: "))
    b = float(input("Введіть другу сторону трикутника: "))
    c = float(input("Введіть третю сторону трикутника: "))
    
    s = (a + b + c) / 2

    area = math.sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))
    print(f"Обрано ТРИКУТНИК. Сторони: {a}, {b}, {c}.")

elif shape == "rectangle":
    w = float(input("Введіть ширину прямокутника: "))
    h = float(input("Введіть висоту прямокутника: "))
    area = w * h
    print(f"Обрано ПРЯМОКУТНИК. Ширина: {w}, Висота: {h}.")

elif shape == "circle":
    r = float(input("Введіть радіус кола: "))
    area = PI * r * r
    print(f"Обрано КОЛО. Радіус: {r}.")

else:
    print(f"Помилка: Невідомий тип фігури '{shape}'.")
    exit()

print(f"Площа: {area:.1f}")
