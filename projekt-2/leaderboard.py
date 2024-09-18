import os

# Funkce pro načtení nejlepších výsledků ze souboru
def load_leaderboard(filename="leaderboard.txt"):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as file:
        leaderboard = []
        for line in file.readlines():
            parts = line.strip().split(",")
            if len(parts) == 2:
                # Pokud záznam nemá čas, nastavíme výchozí hodnotu pro čas (9999 sekund)
                name, guesses = parts
                time = 9999.0
            elif len(parts) == 3:
                name, guesses, time = parts
            else:
                continue  # Přeskočíme záznamy, které nejsou ve správném formátu
            leaderboard.append((name, int(guesses), float(time)))
    return leaderboard

# Funkce pro uložení výsledků do souboru
def save_leaderboard(leaderboard, filename="leaderboard.txt"):
    with open(filename, "w") as file:
        for name, guesses, time in leaderboard[:10]:  # Uložíme jen 10 nejlepších
            file.write(f"{name},{guesses},{time:.2f}\n")

# Funkce pro přidání nového výsledku do leaderboardu
def add_to_leaderboard(name, guesses, time, filename="leaderboard.txt"):
    leaderboard = load_leaderboard(filename)
    leaderboard.append((name, guesses, time))
    # Seřadíme nejprve podle počtu pokusů, pokud je stejný, řadíme podle času
    leaderboard.sort(key=lambda x: (x[1], x[2]))
    save_leaderboard(leaderboard, filename)

# Funkce pro vypsání leaderboardu
def display_leaderboard(filename="leaderboard.txt"):
    leaderboard = load_leaderboard(filename)
    if not leaderboard:
        print("No entries in the leaderboard yet.")
    else:
        print("\nLeaderboard - Top 10:")
        for i, (name, guesses, time) in enumerate(leaderboard[:10], start=1):
            print(f"{i}. {name} - {guesses} guesses, {time:.2f} seconds")
