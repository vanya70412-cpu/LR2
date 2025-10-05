n = int(input("Введіть двоцифрове число (наприклад 55): "))

if abs(n) < 10 or abs(n) > 99:
    print(f"Число {n} не є двоцифровим")
    use_last = input("Бажаєте використати останні дві цифри цього числа (так/ні)? ")
    if use_last.lower() in ("так", "t", "yes", "y"):
        n = abs(n) % 100
        print(f"Використано останні дві цифри: {n:02d}")
    else:
        print("Програма завершена")
        exit()

n_abs = abs(n)
tens = (n_abs // 10) % 10
ones = n_abs % 10
digit_sum = tens + ones

print(f"Цифри: десятки={tens}, одиниці={ones}, сума={digit_sum}")

if 10 <= digit_sum <= 99:
    print("Сума цифр є двоцифровим числом")
else:
    print("Сума цифр не є двоцифровим числом")