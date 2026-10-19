# 2025 styczeń
import random

class SpecialList:
    def __init__(self, length):
        self.itemsCount = length
        for i in range(length):
            self.items.append(random.randint(1, 1000+1))

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

if __name__ == '__main__':
    list_a = SpecialList(25)
    list_a.display_all()
    found = list_a.find_item(10)
    print(f"Razem nieparzystych: {list_a.display_odds()}")
    if found != -1:
        print(f"Liczbę 10 znaleziono na indeks = {found}")
    print(f"Średnia wszystkich elementów: {list_a.calc_average()}")