from time import sleep, time
import os

os.system("clear")

red = '\033[31m'
yellow = '\033[33m'
reset = '\033[0m'

number = int(input("Zadajte nejaké číslo: "))

# Začiatok merania času
start_time = time()

for i in range(0, number + 1):
    print(f"{yellow} Testing : {reset} {red} {i} {reset}")
    sleep(0.000001)

# Koniec merania času
end_time = time()

# Výpočet trvania testovania
elapsed_time = end_time - start_time

print(f"Koniec.")
print(f"Čas trvania: {yellow} {elapsed_time}{reset} sekundy")
