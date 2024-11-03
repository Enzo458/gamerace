import random
import time
import os
from colorama import Fore, Back, Style, init
def carrera():
    init()
    corredor1 = 0
    corredor2 = 0
    meta = 50

    print("¡Bienvenido a la carrera de terminal!")
    print("El primer corredor en alcanzar la meta de 50 gana.")

    while corredor1 < meta and corredor2 < meta:
        time.sleep(0.5)
        corredor1 += random.randint(1, 3)
        corredor2 += random.randint(1, 3)
        os.system("cls")
        print("-"*50)
        print(Fore.RED +   f"{' ' * corredor1}:-:>{' ' * (meta-3 - corredor1)}|$|")
        print(Fore.GREEN + f"{' ' * corredor2}:-:>{' ' * (meta-3- corredor2)}|$|")
        print(Style.RESET_ALL + "-" * 50)
    
    if corredor1 >= meta and corredor2 >= meta:
        print("¡Es un empate!")
    elif corredor1 >= meta:
        print("1. Corredor 1. Win!")
        print(f"2. Corredor 2. {meta - corredor2}.")
    else:
        print("1. Corredor 2. Win!")
        print(f"2. Corredor 1. {meta - corredor1}.")
carrera()

