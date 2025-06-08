from re import search

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

#Домашнее задание
#string = input("Введите текст: ")
#text = string.upper()
#vowels = "АОУЫИЭУЕЁЮЯ"
#vowels_count = 0
#consonant_count = 0
#for char in text:
#    if char.isalpha():
#        if char in vowels:
#            vowels_count += 1
#        else:
#            consonant_count += 1
#print("Количество гласных букв: ", vowels_count)
#print("Количество согласных букв: ", consonant_count)
#words = string.split()
#max_word = ""
#for word in words:
#    clean_word = ""
#    for char in word:
#        if char.isalpha():
#            clean_word += char
#            if len(clean_word) > len(max_word):
#             max_word = clean_word
#print("Самое длинное слово: ", max_word)
#search_word = input("Введите слово для поиска: ")
#normalized_words = []
#for word in words:
#    clean = "".join([c for c in word if c.isalpha()])
#    normalized_words.append(clean)
#    print("Количество вхождений слова: ", normalized_words.count(search_word))

#Процедуры и функции
def greet_and_count(user_name):
    username_clean = user_name.replace(" ", "")
    print(f"Привет, {user_name}! Добро пожаловать!")
    print(f"В твоем имени {len(username_clean)} символов.")
username = input("Пожалуйста, введите ваше имя: ")
greet_and_count(username)









































