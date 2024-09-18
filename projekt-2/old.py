"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Karel Provázek
email: provazek@24s.cz
discord: provazek24s.cz_84357
"""


# generování náhodného čísla
import random

def generate_secret_number():
    digits = list('123456789')  # První číslice nesmí být 0
    secret_number = random.choice(digits)  # První číslo
    digits.append('0')  # 0 může být přidáno zpátky pro další čísla
    secret_number += ''.join(random.sample(digits, 3))  # Další 3 čísla
    return secret_number

# validace vstupu uživatel


def is_valid_guess(guess):
    if len(guess) != 4:
        return False, "Číslo musí mít přesně 4 číslice."
    if not guess.isdigit():
        return False, "Vstup musí obsahovat pouze číslice."
    if guess[0] == '0':
        return False, "Číslo nesmí začínat nulou."
    if len(set(guess)) != 4:
        return False, "Číslice musí být unikátní."
    return True, ""


# vyhodnocení bulls a cows
def evaluate_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((g in secret) for g in guess) - bulls
    return bulls, cows

# hlavní smyčka programu
def main():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret_number = generate_secret_number()
    guesses = 0

    while True:
        guess = input("Enter a number: ")
        valid, message = is_valid_guess(guess)
        if not valid:
            print(message)
            continue

        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-" * 47)

if __name__ == "__main__":
    main()
