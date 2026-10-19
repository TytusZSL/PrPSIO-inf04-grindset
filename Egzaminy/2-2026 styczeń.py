# 2026 styczeń
import random

class Kosc:
    def __init__(self, dots=None):
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

if __name__ == "__main__":
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