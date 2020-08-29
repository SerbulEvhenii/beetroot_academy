from coffecars import Car, Drink
from coffecars.cars import Cars_list
from coffecars.drink import DrinksList

if __name__ == '__main__':

    all_drinks = DrinksList()
    all_cars = Cars_list.restorag('data/dat.json', all_drinks)
    while True:
        '''
        выход
        добавить машину
        добавить напиток
        присвоить напиток машинам
        '''
        action = input("?")
        if action=='q':
            break


