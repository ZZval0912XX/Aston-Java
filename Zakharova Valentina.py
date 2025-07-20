

def greet_user(username):
    # Удаляем пробелы из имени для подсчета символов
    username_clean = username.replace(" ", "")
    # Выводим персонализированное приветствие
    print(f"Привет, {username}! Рады видеть тебя здесь!")
    # Выводим количество символов в имени (без пробелов)
    print(f"Твое имя состоит из {len(username_clean)} символов.")

# Пример использования
user_name = input("Пожалуйста, введите ваше имя: ")
greet_user(user_name)