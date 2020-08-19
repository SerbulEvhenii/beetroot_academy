# Home Work 13.1
def get_local_variables(func):
    print(func.__code__.co_nlocals)

def test_func():
    x = 1
    text = 'Hello'
    PI = 3.14

# Home Work 13.2

def get_name():
    print('Я вложенная функция в другую функцию.')

def get_func_name():
    return get_name()

get_func_name()


# Home Work 13.3

def choose_func(nums, func1, func2):
    for num in nums:
        if num < 0:
            return func2(nums)
    return func1(nums)

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
get_local_variables(test_func)