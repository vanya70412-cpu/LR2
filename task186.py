a = int(input("Введіть перше ціле число: "))
b = int(input("Введіть друге ціле число: "))
c = int(input("Введіть третє ціле число: "))

nums = [a, b, c]
nums.sort()
print(f"Відсортовані числа: {nums}")

p = nums[0] * nums[1]
print(f"Добуток двох найменших чисел {nums[0]} і {nums[1]} = {p}")