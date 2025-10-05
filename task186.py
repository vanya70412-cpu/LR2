def read_int(prompt):
    while True:
        s = input(prompt).strip()
        if s == "":
            print("Порожній ввід — спробуйте ще раз.")
            continue
        try:
            return int(s)
        except ValueError:
            print("Некоректне значення. Введіть ціле число (наприклад: 3 або -5).")


print("Програма: обчислити добуток двох найменших із трьох введених цілих чисел.")
a = read_int("Введіть перше ціле число a: ")
b = read_int("Введіть друге ціле число b: ")
c = read_int("Введіть третє ціле число c: ")

if a == b == c:
    product = a * b
    print(f"Увага: всі три числа однакові ({a}). Добуток двох найменших = {product}")
else:
    nums = [a, b, c]
    nums.sort()
    min1, min2 = nums[0], nums[1]
    product = min1 * min2
    if min1 == 0 or min2 == 0:
        print(f"Серед двох найменших є 0 (числа: {min1}, {min2}). Добуток = 0.")
    else:
        print(f"Два найменші числа (в порядку зростання): {min1}, {min2}")
        print(f"Добуток двох найменших чисел = {product}")

print("Кінець програми.")
