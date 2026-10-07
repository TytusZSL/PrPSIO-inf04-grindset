import random
from random import shuffle


# 2026 czerwiec
def password_generator():
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    polish = ['ą', 'ę', 'ł', 'ń', 'ó', 'ś', 'ż', 'ź', 'Ą', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ż', 'Ź']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

    needed_chars = [[3, lowercase], [3, uppercase], [2, polish], [2, numbers], [2, symbols]]

    print("Wygenerowane hasła: ")
    for i in range(5):
        chosen_chars = []

        for requirement in needed_chars:
            for count in range(0, requirement[0]):
                chosen_chars.append(random.choice(requirement[1]))

        random.shuffle(chosen_chars)
        password = ''.join(list(chosen_chars))

        print(f'{i}. {password}')

# 2026 styczeń
class Kosc:
    def __init__ (self, dots = None):
        if dots is None:
            dots = random.randint(1, 6)
        if dots not in [1, 2, 3, 4, 5, 6]:
            dots = 0
        self.dots = dots
        self.file_name = f'kosc{self.dots}.png'
        self.available = True
        Kosc.dice_count += 1

    def roll_dice(self):
        if self.available:
            self.dots = random.randint(1, 6)
            self.file_name = f'kosc{self.dots}.png'

    def block_dice(self):
        self.available = False

    def display_value(self):
        text_numbers = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć"]
        return text_numbers[self.dots]

    dice_count = 0
    dots = 0
    file_name = ""
    available = True

def die_test():
    die1 = Kosc()
    print(f"Ilość utworzonych kości: {Kosc.dice_count}")
    print(f"Wartość kości: {die1.display_value()} ({die1.dots})")
    print(f"Nazwa pliku: {die1.file_name}")
    try:
        die2 = Kosc(int(input("Podaj wartość drugiej kości (napisz + enter): ")))
    except ValueError:
        die2 = Kosc(0)
    print(f"Ilość utworzonych kości: {Kosc.dice_count}")
    print(f"Wartość kości: {die2.display_value()} ({die2.dots})")
    print(f"Nazwa pliku: {die2.file_name}")

# 2025 czerwiec
def lottery():
    roll_count = int(input("Ile wygenerować losowań? \n"))
    randomized_sets = create_random_numbers(roll_count)
    showcase_results(randomized_sets)

def create_random_numbers(roll_count):
    randomized_sets = []
    for i in range(roll_count):
        cur_set = []
        for l in range(6):
            chosen_number = random.randint(1, 49)
            #reroll until the number is a non-duplicate
            while chosen_number in cur_set:
                chosen_number = random.randint(1, 49)
            cur_set.append(chosen_number)
        randomized_sets.append(cur_set)
    return randomized_sets

def showcase_results(randomized_sets):
    print("Zestawy wylosowanych liczb: ")
    for i in range(len(randomized_sets)):
        print(f"Losowanie {i+1}: {' '.join(str(i) for i in randomized_sets[i])}")
    number_instances = {}
    for num_set in randomized_sets:
        for num in num_set:
            if num not in number_instances:
                number_instances[num] = 1
            else:
                number_instances[num] += 1
    for num in range(1, 50):
        print(f"Wystąpienia liczby {num}: {0 if num not in number_instances else number_instances[num]}")

# 2025 styczeń
def special_list_test():
    list_a = SpecialList(25)
    list_a.display_all()
    found = list_a.find_item(10)
    if found != -1:
        print(f"Liczbę 10 znaleziono na indeks = {found}")
    print(f"Razem nieparzystych: {list_a.display_odds()}")
    print(f"Średnia wszystkich elementów: {list_a.calc_average()}")

class SpecialList:
    def __init__(self, length):
        self.itemsCount = length
        for i in range(length):
            self.items.append(random.randint(1, 1000))

    def display_all(self):
        for i in range(self.itemsCount):
            print(f'{i}: {self.items[i]}')

    def find_item(self, value):
        for i in range(self.itemsCount):
            if self.items[i] == value:
                return i
        return -1

    def display_odds(self):
        odd_count = 0
        print("Liczby nieparzyste:")
        for i in range(self.itemsCount):
            if self.items[i] % 2 == 1:
                odd_count += 1
                print(self.items[i])
        return odd_count

    def calc_average(self):
        items_sum = 0
        for item in self.items:
            items_sum += item
        return items_sum / self.itemsCount

    itemsCount = 0
    items = []

# 2024 czerwiec

if __name__ == '__main__':
    # password_generator()
    # die_test()
    # lottery()
    special_list_test()