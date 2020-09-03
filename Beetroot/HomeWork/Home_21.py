from typing import Optional

print('Home Work 21.1')

def to_power(x, exp: int):
    if exp < 0:
        return 'This function works only with exp > 0.'
    elif exp == 1:
        return x
    else:
        return x * (to_power(x, exp - 1))


print(to_power(5, -1))
print('\nHome Work 21.2')

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1:
        return True
    elif looking_str[0] == looking_str[-1] and len(looking_str) < 3:
        return True
    elif looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False



print(is_palindrome('bbaassaabb'))
print('\nHome Work 21.3')

def mult(a: int, n: int) -> int:
    pass

print('\nHome Work 21.4')
def reverse(str):
    list_word = list(str)
    letter = ''
    # print(list_word)
    if len(list_word) > 1:
        letter = letter + list_word.pop(-1)
        # print(list_word)
        new_str = ''.join(list_word)
        # print(new_str)
    else:
        letter = letter + list_word.pop(1)
    print(letter)
    return letter + reverse(new_str)


    # s = s + str[-1::]
    # return s
    # if len(str) == 1:
    #     return str
    # else:
    #     reverse_str = ''
    #     reverse_str += str[-1]
    #     return reverse(reverse_str)


# print(reverse('hello'))

print('\nHome Work 21.5')
def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        return 'Input string must be digit string'
    elif len(digit_string) == 1:
        return int(digit_string)
    else:
        digit_last_num = int(digit_string) % 10                # отделяем последнюю цифру
        digit_string_to_num = int(digit_string) // 10          # удаляем последнюю цифру у исходного числа
        return digit_last_num + sum_of_digits(str(digit_string_to_num))

print(sum_of_digits('1234'))