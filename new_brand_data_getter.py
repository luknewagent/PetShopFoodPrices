from general_functions import *

def getBrandName() -> str:
    while True:
        print("Nombre de la marca o cero(0) para volver al menu principal")

        name = input(">>").title()
        if name == "0":
            break
        elif name != "":
            return name
        else:
            print("Error: no se puede dejar el nombre vacio.")

def getCostPrice(name) -> int:
    while True:
        print(f"Precio de compra de {name}")

        try:
            costPrice = int(input(">>"))
        except ValueError:
            print("Error: el precio de costo tiene que ser en numeros")
        else:
            return costPrice

def getSalePrice(name) -> int:
    while True:
        print(f"Precio de venta de {name}:")

        try:
            salePrice = int(input(">>"))
        except ValueError:
            print("Error: el precio de venta tiene que estar en numeros")
        else:
            return salePrice

def getKGs(name) -> int:
    while True:
        print(f"Kgs de {name}:")

        try:
            kgs = int(input(">>"))
        except ValueError:
            print("Los kilogramos deben estar en numeros.")
        else:
            return kgs

def getOffer(name) -> bool:
    print(f"{name} esta con oferta? S/N")

    offer = input(">>").upper()
    if offer == "S":
        return True
    else:
        return False