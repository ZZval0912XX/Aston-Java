
#n_string = input("Сколько чисел Фибоначчи хотите получить= ")
#n = int(n_string)
#fib0 = 0
#fib1 = 1
#fib = 0
#i = 0
#while i < n:
#    fib = fib0+fib1
#    print(fib)
#    fib0 = fib1
#    fib1 = fib
#    i = i+1


#for i in range(10,0,-1):
#    print(i)


#input_string = input("Введите строку: ")
#input_string = input_string.lower()
#vowels = 0
#for char in input_string:
#    if char.isalpha():
#        if char in 'аоиеуы':
#            vowels +=1
#            print(f"Количество гласных букв: {vowels}")


#number = 91
#sum_digits = 0
#for i in str(number):
#    sum_digits +=int(i)
#    print(f"Сумма цифр числа: {sum_digits}")


#for i in range(1,11):
#    for j in range(1,11):
#        print(i*j, end='\t')

#letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
#result = ''
#for letter in letters:
#    if letter.islower():
#        result += letter
#        print(result)

#secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
#while True:
#    nickname = input("Для входа введите ваш никнейм: ")
#    if nickname in secret_list:
#        print(f"Ты-свой. Приветсвую любезно. {nickname}!")
#        break
#    else:
#        print("Тут ничего нет. Еще есть вопросы?")

#a=int(input("Введите первое число: "))
#b=int(input("Введите второе число: "))
#if a > b:
#    print("a > b")
#elif a < b:
#    print("a < b")
#else:
#    print("a = b")

#a=int(input("Введите первое число: "))
#b=int(input("Введите второе число: "))
#print("Сумма: ", a + b)
#print("Разность: ", a - b)
#print("Произведение: ", a * b)
#if b == 0:
#    print("На ноль делить нельзя")
#else:
#    print("Деление: ", a / b)

#a=input("Введите первую строку: ").lower()
#b=input("Введите вторую строку: ").lower()
#if sorted(a) == sorted(b):
#    print("Строки идентичны")
#else:
#   print("Строки неидентичны")

#chislo = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
#for x in chislo:
#    if x % 2 == 0:
#        print(x)

# Задача номер 6
#s = input("Введите строку: ")
#no_spaces = s.replace(" ", "")
#print(no_spaces)

# Задача номер 7
#s = input("Введите строку: ").lower()
#words = s.split()
#longest_word = ""
#for word in words:
#    if len(word) > len(longest_word):
#        longest_word = word
#        print(f"Самое длинное слово в строке: {longest_word}")
































