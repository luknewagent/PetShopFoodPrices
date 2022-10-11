import os

def printTitle(title: str):
    os.system("cls")
    print("\t\tADMINISTRADOR DE PRECIOS DE PETSHOP\n")
    print(f"{title}")


def pausa():
    print()
    input("Apreta cualquier tecla para continuar...")


def confirmOption():
    print("Confimar cambio S/N")
    confirmopt = input(">>").upper()
    return confirmopt


def confirmed(confirm_opt):
    return confirm_opt == "S"