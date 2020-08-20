from datetime import datetime


def bin_sum(a,b):
    return sum(bin(i).count('1') for i in range (a,b+1))

def createList(a, b):
    list_1 = []
    if a > b:
        for x in range(b, (a + 1), 1):
            list_1.append(x)
    else:
        for x in range(a, (b + 1), 1):
            list_1.append(x)
    return list_1


def convertBinList(list):
    list_convert = []
    for x in list:
        y = sumBin(decimalToBinary(x))
        list_convert.append(y)
    return list_convert


def decimalToBinary(n):
    return int(bin(n).replace("0b", ""))


def sumBin(n):
    suma = 0
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    return suma


def sumListNumbers(list):
    sum = 0
    for x in list:
        sum += x
    return sum

start1 = datetime.now()

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = createList(a, b)
print(c)
c = convertBinList(c)
print(c)
c = sumListNumbers(c)
print(c)
print(datetime.now() - start1)
start2 = datetime.now()

print(bin_sum(2,7))
print(datetime.now() - start2)