# Home Work 5.1
import random

print('Home Work 5.1')
list_numbers = []
i = 0
while i < 10:
    list_numbers.append(random.randint(0, 100))
    i += 1
list_numbers.sort()
print(list_numbers)
print(f'The maximum number in an array is {list_numbers[-1]}.')

# Home Work 5.2
print('\nHome Work 5.2')
list_numbers_2 = []
list_numbers_3 = []
numbers_2_and_3 = set()
i = 0
while i < 10:
    list_numbers_2.append(random.randint(1, 10))
    list_numbers_3.append(random.randint(1, 10))
    i += 1
print('First list - ', list_numbers_2)
print('Second list - ', list_numbers_3)
while list_numbers_2:
    numbers_2_and_3.add(list_numbers_2.pop())
while list_numbers_3:
    numbers_2_and_3.add(list_numbers_3.pop())
print('Set - ', numbers_2_and_3)

#print('\nHome Work 5.3')
list_numbers_4 = []
list_numbers_5 = []
i = 1
while i < 101:
    list_numbers_4.append(i)
    i += 1
while list_numbers_4:
    a = list_numbers_4.pop()
    if a % 7 == 0 and a % 5 != 0:
        list_numbers_5.append(a)
print(list_numbers_5)
