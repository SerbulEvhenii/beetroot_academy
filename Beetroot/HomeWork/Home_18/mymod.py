def count_lines(name):
    with open(name, 'r') as file:
        list_words = file.read().split()
        sum_words = len(list_words)
        print('Sum words -', sum_words)
        return sum_words


def count_chars(name):
    with open(name, 'r') as file:
        list_words = file.read().split()
        sum_chars = sum(len(word) for word in list_words)
        print('Sum chars -', sum_chars)
        return sum_chars


def test(file_name):
    count_lines(file_name)
    count_chars(file_name)


test('for_Home_18.txt')
