shape = input("Введіть тип кімнати (triangle, rectangle, circle): ").strip().lower()

if shape == "triangle":
    a = float(input("Введіть сторону a: "))
    b = float(input("Введіть сторону b: "))
    c = float(input("Введіть сторону c: "))
    s = (a + b + c) / 2.0
    p = s * (s - a) * (s - b) * (s - c)
    if p <= 0:
        print("Задані сторони не утворюють правильний трикутник")
    else:
        area = p ** 0.5
        print(f"Площа трикутника = {area}")
elif shape == "rectangle":
    l = float(input("Введіть довжину прямокутника: "))
    w = float(input("Введіть ширину прямокутника: "))
    if l <= 0 or w <= 0:
        print("Сторони прямокутника мають бути додатними")
    else:
        print(f"Площа прямокутника = {l * w}")
elif shape == "circle":
    r = float(input("Введіть радіус кола: "))
    if r <= 0:
        print("Радіус має бути додатнім")
    else:
        area = 3.14 * r * r
        print(f"Площа кола = {area}")
else:
    print("Невірний тип фігури, очікується triangle, rectangle або circle")