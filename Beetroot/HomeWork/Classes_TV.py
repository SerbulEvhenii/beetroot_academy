# ВНИМАНИЕ! Извините было мало времени, не успел в методах обработать ошибки по вводу цифр, символов и букв
# чтобы пользователь не сломал программу.
class TV_controller:

    def __init__(self, model, channels):
        self.model = model
        self.channels = channels
        self.selected_channel = 0

    def first_channel(self):
        print(self.channels[0])

    def last_channel(self):
        print(self.channels[-1])

    def turn_channel(self, N):
        if N > len(self.channels) or N < 1:
            print('Такого канала не существует')
        else:
            self.selected_channel = N - 1
            print(self.channels[self.selected_channel])

    def next_channel(self):
        self.selected_channel += 1
        if self.selected_channel >= len(self.channels):
            self.selected_channel = 0
            print(self.channels[self.selected_channel])
        else:
            print(self.channels[self.selected_channel])

    def previous_channel(self):
        self.selected_channel -= 1
        if self.selected_channel < 0:
            self.selected_channel = len(self.channels) - 1
            print(self.channels[self.selected_channel])
        else:
            print(self.channels[self.selected_channel])

    def current_channel(self):
        print('Сейчас включен - ' + self.channels[self.selected_channel])

    def is_exist(self, search):
        self.search = str(search)
        if self.search.isdigit():
            if int(self.search) > len(self.channels) or int(self.search) < 1:
                print('Такого канала нет')
            else:
                print('Да, такой канал есть')
        elif self.search in self.channels:
            print('Да, такой канал есть')
        else:
            print('Такого канала нет')

