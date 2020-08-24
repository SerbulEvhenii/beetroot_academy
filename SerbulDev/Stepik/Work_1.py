# def mix_verses1(file_name):
#   text_file = open(file_name)
#   print(text_file.read())

# mix_verses('stih_1.txt')


def read_verse(file_name):
    with open(file_name) as f:
        for line in f:
            yield line.strip()


def mix_verses(lists):
    list_verses = lists
    my_array_iterators = []
    for num in list_verses:
        my_array_iterators.append(read_verse(num))
    while my_array_iterators:
        try:
            for itr in my_array_iterators:
                print(next(itr))
        except StopIteration:
            pass


def full_mix_verses(*args):
    list_verses = args
    mix_verses(list_verses)


# read_verse('stih_1.txt')
# mix_verses('stih_1.txt', 'stih_2.txt', 'stih_3.txt')
full_mix_verses('stih_1.txt', 'stih_2.txt', 'stih_3.txt')