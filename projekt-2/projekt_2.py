"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Karel Provázek
email: provazek@24s.cz
discord: provazek24s.cz_84357
"""

# Importy
import random
from game_stats import start_timer, end_timer, increment_guesses  # Importy z nového souboru
from leaderboard import add_to_leaderboard, display_leaderboard  # Importy pro práci s leaderboardem

# Funkce pro generování tajného čísla s unikátními číslicemi
def generate_secret_number():
    digits = list('123456789')  # První číslice nesmí být 0
    secret_number = random.choice(digits)  # První číslo
    digits.remove(secret_number)  # Odebereme první číslo z dostupných číslic
    digits.append('0')  # 0 může být přidáno zpátky pro další čísla
    secret_number += ''.join(random.sample(digits, 3))  # Další 3 čísla
    return secret_number

# Funkce pro validaci vstupu uživatele
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

# Funkce pro vyhodnocení bulls a cows
def evaluate_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum((g in secret) for g in guess) - bulls
    return bulls, cows

# Hlavní smyčka hry Bulls and Cows
def play_bulls_and_cows():
    # Nápověda pro hráče
    print("Vítejte ve hře Bulls and Cows!")
    print("Pravidla:")
    print("1. Musíte zadat 4místné číslo.")
    print("2. Číslo nesmí začínat nulou.")
    print("3. Číslice musí být unikátní.")
    print("4. Hra vám řekne, kolik máte 'bulls' (správná číslice na správném místě) a 'cows' (správná číslice, ale na špatném místě).")
    print("-" * 47)

    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)

    secret_number = generate_secret_number()

    # Zobrazení tajného čísla pro testovací účely
   # print(f"Tajné číslo (pro testování): {secret_number}")  # Můžeš zakomentovat, až nebudeš potřebovat

    guesses = 0
    start_time = start_timer()  # Spuštění časovače

    while True:
        guess = input("Enter a number: ")
        valid, message = is_valid_guess(guess)
        if not valid:
            print(message)
            continue

        guesses = increment_guesses(guesses)  # Zvýšení počtu pokusů
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            elapsed_time = end_timer(start_time)  # Zastavení časovače
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            print(f"Time taken: {elapsed_time:.2f} seconds")

            # Přidání výsledku na leaderboard
            name = input("Enter your name for the leaderboard: ")
            add_to_leaderboard(name, guesses, elapsed_time)

            # Zobrazení leaderboardu
            display_leaderboard()

            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-" * 47)

# Spuštění hry
if __name__ == "__main__":
    play_bulls_and_cows()
