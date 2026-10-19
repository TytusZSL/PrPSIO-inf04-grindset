# 2026 czerwiec
import random

if __name__ == '__main__':
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
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