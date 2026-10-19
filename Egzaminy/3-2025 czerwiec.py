# 2025 czerwiec
import random

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

if __name__ == "__main__":
    required_rolls = int(input("Ile wygenerować losowań? \n"))
    rolled_sets = create_random_numbers(required_rolls)
    showcase_results(rolled_sets)