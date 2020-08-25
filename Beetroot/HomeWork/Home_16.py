# Home Work 16.1

list1 = [1, 4, 6, 4, 6, 1, 24, 246, 11]
dict1 = {'val1': 5,
         'val2': 63,
         'val3': 123
         }

def with_index(iterable, start=0):
    for i in iterable:
        print(f'{start} {i}')
        start += 1


print('Home Work 16.1')
with_index(list1, 10)
print('')
with_index(dict1, 100)


# Home Work 16.2
print('\nHome Work 16.2')
def in_range(start, end, step=1):
    while start < end:
        print(start)
        start += step

in_range(5, 20, 2)


# Home Work 16.3
print('\nHome Work 16.3')

a = (x**2 for x in range(1000000))
print(a)


# class MyIter:
#     for i in MyIter(10):
#         print(i)
#     b = MyIter(20)
#     print(b[15])
#
# dunder method index