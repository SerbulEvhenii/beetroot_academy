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
            print(text)
        return wrapper
    return func_stop


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan('Steve')
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"



print('\nHome Work 14.3')