import math
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
#def greet_and_count(user_name):
#    username_clean = user_name.replace(" ", "")
#    print(f"Привет, {user_name}! Добро пожаловать!")
#    print(f"В твоем имени {len(username_clean)} символов.")
#username = input("Пожалуйста, введите ваше имя: ")
#greet_and_count(username)

#def print_dashes(N):
#    if N > 0:
#        line = "-" * N
#        print(line)
#        print(line)
#    else:
#        print("Число N должно быть натуральным (N > 0)")
#print_dashes(3)

#def print_triangle():
#    N = int(input("Введите размер стороны треугольника (N): "))
#    for i in range(1, N + 1):
#        print('*' * i)
#print_triangle()

#def hislo_max (a, b, c, d, e, f):
#    return max(a, b, c, d, e, f)
#print(hislo_max(22, 5, 3, 8, 4, 2))

#def circle_area(radius):
#    return 3.14 * radius ** 2
#print(f"Площадь круга с радиусом 7: {circle_area(7):.2f}")

# № 4
#def average_of_five_numbers(numbers):
#    return sum(numbers) / len(numbers)
#numbers = [10, 10, 10, 10, 10]
#result = average_of_five_numbers(numbers)
#print("Среднее арифметическое: ", result)

# № 5
#def count_digits(number):
#    num_str = str(abs(number))
#    return len(num_str)
#print(count_digits(12345))
#print(count_digits(-9876))
#print(count_digits(0))

# № 7
#def distance (x1, y1, x2, y2):
#    return (((x2 - x1)** 2) + ((y2 -y1)** 2))** 0.5
#def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#    a = distance(x1, y1, x2, y2)
#    b = distance(x2, y2, x3, y3)
#    c = distance(x3, y3, x1,y1)
#    return a + b + c
#print(triangle_perimetr(x1=1,y1=2,x2=2,y2=3,x3=4,y3=2))


# № 11
#def swap_values(a, b, c, d):
#    a, b = b, a
#    c, d = d, c
#    return a, b, c, d
#a = 1
#b = 2
#c = 3
#d = 4
#print("До обмена: ", a, b, c, d)
#a, b, c, d = swap_values(a, b, c, d)
#print("После обмена: ", a, b, c, d)

# № 12
#def calculate_triangle_perimeter(a, b, c):
#    perimeter = a + b + c
#    return perimeter
#print(calculate_triangle_perimeter(a=1, b=2, c=4))

#def calculate_triangle_area(a, b, c):
#    if a <= 0 or b <= 0 or c <= 0:
#        raise ValueError("Длины сторон должны быть положительными числами")
#    if a + b <= c or a + c <= b or b + c <= a:
#        raise ValueError("Сумма любых двух сторон должна быть больше третьей стороны")
#    s = (a + b + c) / 2
#    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#    return area
#print(calculate_triangle_area(a=3, b=4, c=5))

# Задача 19
#def pointInRect(px, py, rect_x1, rect_y1, rect_x2, rect_y2):
#    left = min(rect_x1, rect_x2)
#    right = max(rect_x1, rect_x2)
#    top = min(rect_y1, rect_y2)
#    bottom = max(rect_y1, rect_y2)
#    return (left <= px <= right) and (top <= py <= bottom)
#print(pointInRect(3, 3, 1, 4, 5, 2))
#print(pointInRect(0, 3, 1, 4, 5, 2))

# Задача 20
#def side_length(x1, y1, x2, y2):
#    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
#def heron_triangle_area(a, b, c):
#    p = (a + b + c) / 2
#    return (p * (p - a) * (p - b) * (p - c))**0.5
#
#def pointinTriangle(px, py, x1, y1, x2, y2, x3, y3):
#    # Стороны и площадь исходного треугольника ABC
#    a = side_length(x1, y1, x2, y2)
#    b = side_length(x2, y2, x3, y3)
#    c = side_length(x3, y3, x1, y1)
#    area_abc = heron_triangle_area(a, b, c)
#
#    # Стороны и площадь треугольника PAB
#    a1 = side_length(px, py, x1, y1)
#    b1 = side_length(px, py, x2, y2)
#    c1 = side_length(x1, y1, x2, y2)
#    area_pab = heron_triangle_area(a1, b1, c1)
#
#    # Стороны и площадь треугольника PBC
#    a2 = side_length(px, py, x2, y2)
#    b2 = side_length(px, py, x3, y3)
#    c2 = side_length(x2, y2, x3, y3)
#    area_pbc = heron_triangle_area(a2, b2, c2)
#
#    # Стороны и площадь треугольника PCA
#    a3 = side_length(px, py, x3, y3)
#    b3 = side_length(px, py, x1, y1)
#    c3 = side_length(x3, y3, x1, y1)
#    area_pca = heron_triangle_area(a3, b3, c3)
#
#    total_area = area_pab + area_pbc + area_pca
#
#    return round(total_area, 5) == round(area_abc, 5)
#
#print(pointinTriangle(1, 1, 0, 0, 4, 0, 0,3))

# Задача 21
#def calculate_final_score(score1, score2, score3, score4, score5):
#    scores = [score1, score2, score3, score4, score5]
#    scores.remove(min(scores))
#    scores.remove(max(scores))
#    final_score = sum(scores) / len(scores)
#    return final_score
#final_score = calculate_final_score(90, 95, 85, 100, 80)
#print(final_score)

# рекурсивные функции
#def fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return fibonacci(n -1) + fibonacci(n - 2)
#    print(fibonacci(0))
#    print(fibonacci(1))
#    print(fibonacci(5))
#    print(fibonacci(10))

# Классы Задание 1
#class Rectangle:
#    def __init__(self, width, height):
#        self.width = width
#        self.height = height
#
#    def area(self):
#        return self.width * self.height
#
#    def perimeter(self):
#        return 2 * (self.width + self.height)
#
#
#class Square(Rectangle):
#    def __init__(self, side):
#        super().__init__(side, side)
#        self.side = side
#
#if __name__ == "__main__":
#    rectangle = Rectangle(4, 5)
#    print("Rectangle:")
#    print("Width:", rectangle.width)
#    print("Height:", rectangle.height)
#    print("Area:", rectangle.area())
#    print("Perimeter:", rectangle.perimeter())
#
#    print("\nSquare:")
#    square = Square(3)
#    print("Side:", square.side)
#    print("Area:", square.area())
#    print("Perimeter:", square.perimeter())
# Задание 2
#class Person:
#    def __init__(self, name, age, gender):
#        self.name = name
#        self.age = age
#        self.gender = gender
#
#    def introduce(self):
#        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет, я {self.gender}.")
#
#
#class Employee(Person):
#    def __init__(self, name, age, gender, salary, position):
#        super().__init__(name, age, gender)
#        self.salary = salary
#        self.position = position
#
#    def work(self):
#        print(f"Я {self.position} и моя зарплата составляет {self.salary} рублей.")
#
#person = Person("Антон", 30, "мужчина")
#person.introduce()
#
#employee = Employee("Валентина", 28, "женщина", 50000, "тестировщик")
#employee.introduce()
#employee.work()







































