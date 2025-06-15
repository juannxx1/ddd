#!/usr/bin/env python3
import random


def main():
    print("Bienvenido a 'Adivina el número'!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina un número entre 1 y 100: "))
            intentos += 1
        except ValueError:
            print("Por favor introduce un número válido.")
            continue

        if intento < numero_secreto:
            print("Demasiado bajo! Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Demasiado alto! Intenta de nuevo.")
        else:
            print(f"Felicidades! Adivinaste el numero {numero_secreto} en {intentos} intentos.")
            break


if __name__ == "__main__":
    main()
