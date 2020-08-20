print("Home Work 10.1")


class Person:
    def __init__(self, firstName, secondName, age):
        self.firstName = firstName.title()
        self.secondName = secondName.title()
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstName} {self.secondName} and I’m {self.age} years old')


person_1 = Person("evhenii", "serbul", 25)
person_1.talk()

print("\nHome Work 10.2")


class Dog():
    age_factor = 7

    def __init__(self, age):
        self.dog_age = age

    def humanAge(self):
        print(f'Dog’s age in human equivalent - {self.age_factor * self.dog_age}')


dog_1 = Dog(14)
dog_1.humanAge()
