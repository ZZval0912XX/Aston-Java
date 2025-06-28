# Задача 1

#def compute_gcd(a, b):
#    while b:
#        a, b = b, a % b
#    return a
#num1 = int(input("Введите первое число: "))
#num2 = int(input("Введите второе число: "))
#gcd = compute_gcd(num1, num2)
#print(f"Наибольший общий делитель чисел {num1} и {num2} равен {gcd}")

# Задача 2

num1 = float(input("Введите первое число: "))
operator = input("Введите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Ошибка: неверный оператор!"
print("Результат:", result)
