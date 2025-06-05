a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
if a > b:
    print("a > b")
elif a < b:
    print("a < b")
else:
    print("a = b")

a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
print("Сумма: ", a + b)
print("Разность: ", a - b)
print("Произведение: ", a * b)
if b == 0:
    print("На ноль делить нельзя")
else:
    print("Деление: ", a / b)

a=input("Введите первую строку: ").lower()
b=input("Введите вторую строку: ").lower()
if sorted(a) == sorted(b):
    print("Строки идентичны")
else:
   print("Строки неидентичны")

chislo = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
for x in chislo:
    if x % 2 == 0:
        print(x)
