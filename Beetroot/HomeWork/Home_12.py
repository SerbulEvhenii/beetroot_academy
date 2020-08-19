import fractions


# Home Work 12.1
print('Home Work 12.1')
class Animal:
    def talk(self):
        print('Издает звук!')


class Dog(Animal):
    def talk(self):
        print('Гав! Гав!')


class Cat(Animal):
    def talk(self):
        print('Мяу! Мяу!')


def animals_song(animal):
    animal.talk()


cat1 = Cat()
dog1 = Dog()

animals_song(cat1)
animals_song(dog1)


# Home Work 12.2
print('\nHome Work 12.2')

class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def __str__(self):
        return f"""
Библиотека "{self.name}" содержит следующую литературу:
{self.authors}
"""

    def __repr__(self):
        return f"""
Библиотека "{self.name}" содержит следующую литературу:
{self.authors}
"""

    def new_book(self, name: str, year: int, author):
        return Book(name, year, author)

    def group_by_author(self, author):
        for x in self.authors:
            if author == x.name:
                return print(f'В нашей библиотеке есть следующие книги писателя {author}: {x.books}')

    def group_by_year(self, year: int):
        ls_books = []
        for x in self.books:
            if year == x.year:
                ls_books.append(x.name)
        return print(f'В нашей библиотеке есть следующие книги {year} года: {ls_books}')


class Book:
    count_books = 0
    list_books = []

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.list_books.append(self)
        Book.count_books += 1

    def __str__(self):
        return f"""
Название книги   - {self.name}
Год написания    - {self.year}
Автор книги      - {str((self.author).name).title()}"""

    def __repr__(self):
        return f"""
Название книги   - {self.name}
Год написания    - {self.year}
Автор книги      - {str((self.author).name).title()}
----------------------"""

    def count_books_numbers(self):
        print(f'Создано книг - {Book.count_books}шт.')


class Author:
    list_authors = []

    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
        Author.list_authors.append(self)

    def __str__(self):
        return f"""
Имя писателя        - {self.name}
Страна рождения     - {self.country}
Дата рождения       - {self.birthday}
Книги               - {self.books}
"""

    def __repr__(self):
        return f"""
Имя писателя        - {self.name}
Страна рождения     - {self.country}
Дата рождения       - {self.birthday}
Книги               - {self.books}
----------------------"""


mihail_bulgakov_books = ['Мастер и Маргарита', 'Собачье сердце', 'Записки юного врача']
mihail_bulgakov = Author('Михаил Булгаков', 'Россия', '15 мая 1891', mihail_bulgakov_books)
master_i_margarita = Book('Мастер и Маргарита', 1928, mihail_bulgakov)
alexander_pushkin_books = ['Капитанская дочка', 'Руслан и Людмила', 'Дубровский', 'Пиковая дама']
alexander_pushkin = Author('Александр Пушкин', 'Россия', '26 мая 1799', alexander_pushkin_books)
dubrovskiy = Book('Дубровский', 1841, alexander_pushkin)
vystrel = Book('Выстрел', 1841, alexander_pushkin)

print(master_i_margarita)
print(mihail_bulgakov)

Book.count_books_numbers(Book)

rus_library = Library('Классическая русская литература', Book.list_books, Author.list_authors)
rus_library.group_by_author('Александр Пушкин')
rus_library.group_by_author('Михаил Булгаков')
rus_library.group_by_year(1841)
rus_library.new_book('Записки юного врача', 1925, mihail_bulgakov)

Book.count_books_numbers(Book)

print(rus_library)


# Home Work 12.3

class Fraction():

    def sum(self, x, y):
        try:
            return print('Сумма: ', x + y)
        except:
            print('В аргумент функции не была передана цифра.')

    def minus(self, x, y):
        try:
            return print('Вычитание ', x - y)
        except:
            print('В аргумент функции не была передана цифра.')

    def mult(self, x, y):
        try:
            return print('Умножение: ', x * y)
        except:
            print('В аргумент функции не была передана цифра.')

    def division(self, x, y):
        try:
            return print('Деление ', x / y)
        except:
            print('В аргумент функции не была передана цифра.')


x = fractions.Fraction(1, 2)
y = fractions.Fraction(1, 4)

print('\nHome Work 12.3')
a = Fraction()
a.sum(x, y)
a.minus(x, y)
a.mult(x, y)
a.division(x, y)
