def oops(list, index):
    print('Начало работы функции oops.')
    print(list[index])


def home_8(list, index):
    print('Начало работы функции home_8.')
    try:
        oops(list, index)
    except IndexError:
        print('Ошибка! Вы передали индекс листа за пределами значений листа.')


people = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]
home_8(people, 12)


def two_numbers():
    try:
        a = int(input())
        b = int(input())
        return print(a ** 2 / b)
    except ZeroDivisionError:
        print('Ошибка! Вы хотите поделить на 0.')
    except ValueError:
        print('Ошибка! Вы ввели букву вместо числа.')


two_numbers()
