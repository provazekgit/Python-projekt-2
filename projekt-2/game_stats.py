import time

# Funkce pro spuštění časovače
def start_timer():
    return time.time()

# Funkce pro ukončení časovače a vrácení uplynulého času
def end_timer(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

# Funkce pro počítání pokusů
def increment_guesses(guesses):
    return guesses + 1
