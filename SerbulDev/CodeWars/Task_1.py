like = ['Petya', 'Vasya', 'Jeka', 'Jora']
def likes(names):
    list_names = names
    if len(list_names) == 1:
        return list_names[0], 'likes this'
    elif len(list_names) == 2:
        return list_names[0], 'and', list_names[1], 'like this'
    elif len(list_names) == 3:
        return list_names[0], list_names[1], 'and', list_names[2], 'like this'
    elif len(list_names) > 3:
        return list_names[0], list_names[1], 'and 2 others like this'
    else:
        return 'no one likes this'

likes([])
likes(['Peter'])
likes(['Jacob', 'Alex'])
likes(['Max', 'John', 'Mark'])
likes(['Alex', 'Jacob', 'Mark', 'Max'])