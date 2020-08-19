# Home Work 4.1
import random

print('Home Work 4.1')
user_number = input('Привет. Я загадал число от 0 до 10, попробуй угадать. Как думаешь какое это число?\n')
random_number = random.randrange(1, 10)

while not str(user_number).isdigit() or user_number != str(random_number):
    if '-' in user_number:
        print('Не нужно вводить отрицательное число. Число загадано от 0 до 10. Пробуй еще раз:')
    elif not str(user_number).isdigit():
        print('Давай не балуйся, вводи цифру, а не буквы. Пробуй еще раз:')
    elif user_number != str(random_number):
        print('Не угадал. Пробуй еще раз:')
    user_number = input()
print('Поздравляю! Ты угадал число.\n')

# Home Work 4.2
print('Home Work 4.2')
user_name = input('Введите ваше имя: ')
user_birthday = int(input('Введите ваш возраст: '))
print(f'Hello {user_name.title()}, on your next birthday you’ll be {user_birthday + 1} years.\n')

# Home Work 4.3
print('Home Work 4.3')
word = input('Введите любое слово: ')
print(random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word),
      random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word),
      random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word),
      random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word),
      random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word) + random.choice(word),
      sep=', ')

# Home Work 4.4
print('\nHome Work 4.4')
print('Добро пожаловать в математическую викторину.')
i = 1
while i == 1:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    input_number = input(f'Сколько будет: {a} + {b} ? \n')
    if '-' in input_number:
        print('Подумай головой. Здесь же сумма чисел, как может быть отрицательное число?. Пробуй еще раз:')
    elif not str(input_number).isdigit():
        print('Давай не балуйся, вводи цифру, а не буквы. Пробуй еще раз.')
    elif int(input_number) == (a + b):
        print('Поздравляем! Это правильный ответ. Хочешь еще раз сыграть? Напиши "Да" или "Нет".\n')
        quit = input()
        if quit.lower() == "да":
            continue
        else:
            i = 0
    else:
        print(f'Ваш ответ неверный, правильный ответ - {a} + {b} = {a + b}. ')
        print('Давай попробуем еще раз.')
