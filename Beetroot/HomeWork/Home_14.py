from functools import wraps

print('Home Work 14.1')


def logger(func):
    @wraps(func)
    def wrapper(*args):
        t = str(args).replace('(', '')
        t = t.replace(')', '')
        print(func.__name__, 'called with', t)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def squareAll(*args):
    return [arg ** 2 for arg in args]


add(10, 25)
squareAll(5, 2, 6, 10, 55)

print('\nHome Work 14.2')


def stop_words(words: list):
    def func_stop(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            for x in words:
                text = text.replace(x, '*')
            return text

        return wrapper

    return func_stop


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('Steve')
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print('\nHome Work 14.3')


def arg_rules(type_: str, max_length: int, contains: list):
    def check(func):
        @wraps(func)
        def wrapper(name):
            if type(name) != type_:
                print('Не верно указан тип данных')
            if len(name) > max_length:
                print('Длина превышена')
            for symbol in contains:
                if not symbol in name:
                    print('Проверка на символы не прошла')
            func(name)

        return wrapper

    return check


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan_2(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan_2('johndoe05@gmail.com') is False
assert create_slogan_2('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
