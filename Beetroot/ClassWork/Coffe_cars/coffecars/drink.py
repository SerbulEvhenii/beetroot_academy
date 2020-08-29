


class Drink:
    def __init__(self, name):
        self.name = name
        self.cars = []
    '''
    name
    price
    cars_list

    store
    restore
    '''
    def __eq__(self, other):
        return isinstance(other, Drink) and self.name == other.name

    def setCar(self, car):
        from coffecars import Car
        if isinstance(car, Car) and car not in self.cars:
            self.cars.append(car)


class DrinksList:

    def __init__(self):
        self.__all_drinks = []

    def getDrinkByName(self, name='tea') -> Drink:
        if Drink(name) not in self.__all_drinks:
            drink = Drink(name)
            self.__all_drinks.append(drink)
            return drink
        else:
            for drink in self.__all_drinks:
                if drink.name == name:
                    return drink
            # return self.__all_drinks[self.__all_drinks.index(Drink(name))]