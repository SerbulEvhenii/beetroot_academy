# Home Work 6.1
print('Home Work 6.1')
str_input_2 = str(input()).lower()
str_input_2 = str_input_2.replace(',', '')
str_input_2 = str_input_2.replace('.', '')
str_input_2_list = str_input_2.split()
dict_word_count = {}
for word in str_input_2_list:
    if dict_word_count.get(word, None) == None:
        dict_word_count[word] = 1
    elif dict_word_count.get(word, None) != None:
        dict_word_count[word] = dict_word_count.get(word) + 1

print(dict_word_count)

# Home Work 6.2
print('\nHome Work 6.2')


def sum_items(dict_1, dict_2):
    'This function computes and returns the total price of stock'
    for key in dict_1:
        print(f'{key.title()} - {dict_1[key] * dict_2[key]}')


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

sum_items(stock, prices)

# Home Work 6.3
print('\nHome Work 6.3')
tuple_double_list = ([x for x in range(1, 11)], [x ** 2 for x in range(1, 11)])
print(tuple_double_list)