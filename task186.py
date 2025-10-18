print('*** Добуток двох найменших з трьох різних цілих чисел ***')
num1 = int(input('Введіть перше число: '))
num2 = int(input('Введіть друге число: '))
num3 = int(input('Введіть третє число: '))

largest = 0

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

product = (num1 * num2 * num3) // largest

print(f"Введені числа: {num1}, {num2}, {num3}")
print(f"Найбільше число: {largest}")
print(f"Добуток двох найменших чисел дорівнює: {product}")
