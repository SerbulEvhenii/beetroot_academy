# Home Work 16.1

list1 = [1, 4, 6, 4, 6, 1, 24, 246, 11]

def with_index(iterable, start=0):
    start_index = start
    for i in iterable:
        print(f'{start_index} {i}')
        start_index += 1

print('Home Work 16.1')
with_index(list1, 10)


# Home Work 16.2
print('\nHome Work 16.2')
def in_range(start, end, step=1):
    num = 0
    while start < end:
        print(start)
        start += step

in_range(5, 20, 2)


# Home Work 16.3
print('\nHome Work 16.3')

a = (x**2 for x in range(1000000))
print(a)

