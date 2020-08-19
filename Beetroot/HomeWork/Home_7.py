# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie.
# The function should then print “My favorite movie is named {name}”.
print('Home Work 7.1')


def favorite_movie():
    like_movie = input("What's your favorite movie?\n")
    print(f'My favorite movie is named {like_movie}.')


favorite_movie()

# Create a function called make_country, which takes in a country’s name and capital as parameters.
# Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
# Make the function print out the values of the dictionary to make sure that it works as intended.
print('Home Work 7.2')


def make_country(name_country, name_capital):
    country = {
        'Name': name_country,
        'Capital': name_capital
    }
    print(f"Country - {country.get('Name')}, capital - {country.get('Capital')}")


make_country('Ukraine', 'Kiyv')

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# - the call make_operation(‘+’, 7, 7, 2) should return 16
# - the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# - the call make_operation(‘*’, 7, 6) should return 42
print('Home Work 7.3')


def make_operation(operation, *args):
    total = 0
    total_2 = 1
    if str(operation) == '+':
        for i in args:
            total = i + total
        return total
    elif operation == '-':
        for i in args[1:]:
            total = i - total
        return total
    elif operation == '*':
        for i in args:
            total_2 *= i
        return total_2
    elif operation == '/':
        for i in args:
            total = i / total
        return total


a = make_operation('+', 7, 7, 2)
b = make_operation('-', 5, 5, -10, -20)
c = make_operation('*', 7, 6)
print(a)
print(b)
print(c)
