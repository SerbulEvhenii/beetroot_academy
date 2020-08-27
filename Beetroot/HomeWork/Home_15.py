import re
import functools

print('Home Work 15.1')


class HomeWork_1():

    def __init__(self, email: str):
        self._email = self.validate(email)

    def validate(self, email: str):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not (re.search(regex, email)):
            print('Вы ввели не валидный email.')
        else:
            print('Вы ввели валидный email.')
            return email


a = HomeWork_1('serbul@gmail.com')

print('\nHome Work 15.2')


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, new_worker):
        if new_worker in self._workers:
            print(f'Рабочий {new_worker.name} уже есть в списке босса {self.name}')
        else:
            if str(new_worker.boss.name) == str(self.name):
                print(f'Рабочий {new_worker.name} добавлен к боссу {self.name}.')
                return self._workers.append(new_worker)
            else:
                print('У рабочего другой босс!')

    def name_class(self):
        return super.__class__.__name__


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss


Jeremy = Boss(1, 'Jeremy', 'Atlantik')
Henry = Boss(2, 'Henry', 'Atlantik')
JonyWalker = Worker(100, 'Jony', 'Atlantik', Jeremy)
GaryHope = Worker(101, 'Gary', 'Atlantik', Jeremy)
LizaRapid = Worker(102, 'Liza', 'Atlantik', Jeremy)
AlexTuz = Worker(103, 'Alex', 'Atlantik', Henry)
Jeremy.workers = JonyWalker
Jeremy.workers = GaryHope
Jeremy.workers = LizaRapid
Jeremy.workers = LizaRapid
Jeremy.workers = AlexTuz

print('\nHome Work 15.3')


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @functools.wraps(func)
        def call_int(*args, **kwargs):
            print('Covert to int')
            try:
                x = func(*args, **kwargs)
                return int(x)
            except:
                print('Ошибочка с данными')

        return call_int

    @staticmethod
    def to_str(func):
        @functools.wraps(func)
        def call_str(*args, **kwargs):
            print('Covert to int')
            try:
                x = func(*args, **kwargs)
                return str(x)
            except:
                print('Ошибочка с данными')
        return call_str

    @staticmethod
    def to_bool(func):
        @functools.wraps(func)
        def call_bool(*args, **kwargs):
            print('Convert to bool')
            try:
                x = func(*args, **kwargs)
                return bool(x)
            except:
                print('Ошибочка с данными')
        return call_bool

    @staticmethod
    def to_float(func):
        @functools.wraps(func)
        def call_float(*args, **kwargs):
            print('Convert to float')
            try:
                x = func(*args, *kwargs)
                return float(x)
            except:
                print('Ошибочка с данными')
        return call_float



@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing(25) == 25
assert do_something('True') is True
