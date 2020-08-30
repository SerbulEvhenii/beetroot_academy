# Я не понял в задании следующее:
# Test your module interactively, using import and name qualification to fetch your exports.
# Does your PYTHONPATH need to include the directory where you created mymod.py?
# Try running your module on itself: e.g., test("mymod.py"). Note that the test opens the file twice;
# if you’re feeling ambitious, you may be able to improve this by passing an open file object into the two count
# functions (hint: file.seek(0) is a file rewind).

print('Home Work 18.3')

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
