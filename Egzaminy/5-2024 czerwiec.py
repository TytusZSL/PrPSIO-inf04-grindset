# 2024 czerwiec
import random

def count_points(dice_list):
    points = 0
    previous_dice = {}
    for dice in dice_list:
        if dice not in previous_dice:
            previous_dice[dice] = True
        else:
            points += dice
            if previous_dice[dice]:
                previous_dice[dice] = False
                points += dice
    return points

if __name__ == '__main__':
    dice_to_roll = 0
    # 1.
    while not (3 <= dice_to_roll <= 10):
        try:
            dice_to_roll = int(input("Ile kostek chcesz rzucić?(3 - 10)\n"))
        except ValueError:
            dice_to_roll = 0

    user_action = "t"
    while user_action == "t":
        user_action = ""
        # 2.
        rolled_dice = [random.randint(1, 6) for _ in range(dice_to_roll)]

        # 3.
        for i in range(1, dice_to_roll + 1):
            print(f"Kostka {i}: {rolled_dice[i-1]}")

        # 4.
        print(f"Liczba uzyskanych punktów: {count_points(rolled_dice)}")

        # 5.
        while user_action not in ["t", "n"]:
            user_action = input("Jeszcze raz? (t/n)\n")