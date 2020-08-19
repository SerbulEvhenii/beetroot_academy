# Home Work 11.1
class Person:
    def __init__(self, name, second_name):
        self.name = name
        self.second_name = second_name
        self.phone_number = 0
        self.email = ''


class Student(Person):
    def __init__(self, name, second_name, kafedra):
        Person.__init__(self, name, second_name)
        self.kafedra = kafedra
        self.num_student_card = 0
        self.average_score = 0


class Teacher(Person):
    def __init__(self, name, second_name):
        Person.__init__(self, name, second_name)
        self.salary = 0
        self.position = ''


# Home Work 11.2
class Mathematician:
    def square_nums(self, list):
        for x in range(len(list)):
            list[x] = list[x] * list[x]
        return list

    def remove_positives(self, list):
        list_numbers_negative = []
        for x in range(len(list)):
            if list[x] < 0:
                list_numbers_negative.append(list[x])
        return list_numbers_negative

    def filter_leaps(self, list):
        years = []
        for x in range(len(list)):
            if list[x] % 4 == 0:
                years.append(list[x])
        return years


# Home Work 11.3
# Product Store

store_amount = {}
store_price = {}


class Product:

    def __init__(self, type_prod, name, price):
        self.type = str(type_prod).lower()
        self.name = name
        self.price = int(price)

    def get_info_product(self):
        print(f'Тип товара: {str(self.type).title()}, название товара - {self.name}, цена - {self.price}$. ')


class ProductStore:
    INCOME = 0

    def add(self, product, amount):
        store_amount[product.name] = amount
        store_price[product.name] = product.price * 1.3

    def set_discount(self, identifier, percent, identifier_type='name'):
        for x in store_price:
            if identifier == x:
                store_price[identifier] = store_price[identifier] - (store_price[identifier] / 100 * percent)
                print(
                    f'Для товара {identifier} добавлена скидка {percent}%. Новая цена товара - {store_price[identifier]}.')

    def sell_product(self, product_name, amount):
        for x in store_amount:
            if product_name == x:
                if amount <= store_amount[product_name]:
                    store_amount[x] = (store_amount[product_name] - amount)
                    self.INCOME = amount * store_price[product_name]
                    print(f'Продано - {product_name} - {amount}шт.')
                else:
                    print('Недостаточно товара для продажи.')

    def get_income(self):
        print(f'На данный момент прибыль магазина: {self.INCOME}$')

    def get_all_products(self):
        print('В магазине есть следующие товары:')
        for key in store_amount:
            print('-', key, '-', store_price[key], '$, в наличии', store_amount[key], 'шт.')

    def get_product_info(self, product_name):
        if product_name in store_amount:
            print('Товар:', product_name.title(), '-', store_amount[product_name], 'шт. на складе, по цене',
                  store_price[product_name], '$')


# Home Work 11.4
class CustomException(Exception):
    def __init__(self, msg):
        self = open('logs.txt', 'w')
        self.write(msg)

try:
    A = int(input('Введите число: \n'))
except:
    msg1 = 'Введены буквы вместо числа.'
    CustomException(msg1)



list_num = [7, 11, 5, 4]
list_neg_num = [26, -11, -8, 13, -90]
years = [2001, 1884, 1995, 2003, 2020]
a = Mathematician()
print(a.square_nums(list_num))
print(a.remove_positives(list_neg_num))
print(a.filter_leaps(years))

iphone_10 = Product('smartphone', 'Iphone 10', 900)
iphone_11 = Product('smartphone', 'Iphone 11', 1100)
tv_LG_450 = Product('TV', 'LG 450', 980)
tv_Samsung_k130 = Product('TV', 'Samsung k130', 2100)
clothing_T_Shirt_adidas_sport = Product('clothing', 'Adidas Sport ultra', 45)
shoes_nike_run100 = Product('shoes', 'Nike Run 100', 245)

Serbul_Store = ProductStore()
Serbul_Store.add(iphone_11, 10)
Serbul_Store.add(iphone_10, 15)
Serbul_Store.add(tv_LG_450, 9)
Serbul_Store.add(clothing_T_Shirt_adidas_sport, 25)

iphone_11.get_info_product()
Serbul_Store.sell_product(iphone_10.name, 3)
Serbul_Store.get_all_products()
Serbul_Store.get_product_info('Iphone 10')
Serbul_Store.get_income()
Serbul_Store.sell_product(iphone_11.name, 6)
Serbul_Store.get_income()
Serbul_Store.set_discount(iphone_10.name, 30)
