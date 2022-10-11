from general_functions import *
from brand import Brand
from general_functions import confirmOption

class BrandCreator:
    def addBrand(self, brands: dict):
        printTitle("AGREGAR UNA MARCA")


        name = self.getBrandName()
        if name == None:
            return
        else:
            print(f"Queres agregar la marca {name}? S/N")
            confirm_opt = input(">>").title()
            if not confirmed(confirm_opt):
                return
        purchasePrice = self.getPurchasePrice(name)

        salePrice = self.getSalePrice(name)

        kgs = self.getKGs(name)

        offer = self.getOffer(name)

        new_brand = Brand(name, purchasePrice, salePrice, kgs, offer)
        brands[name] = new_brand

    def getBrandName(self):
        while True:
            print("Nombre de la marca o cero(0) para volver al menu principal")
            name = input(">>").title()
            if name == "0":
                break
            elif name != "":
                return name
            else:
                print("Error: no se puede dejar el nombre vacio.")

    def getPurchasePrice(self, name):
        while True:
            print(f"Precio de compra de {name}")

            try:
                purchasePrice = int(input(">>"))
            except ValueError:
                print("Error: el precio de compra tiene que ser en numeros")
            else:
                return purchasePrice

    def getSalePrice(self, name):
        while True:
            print(f"Precio de venta de {name}:")

            try:
                salePrice = int(input(">>"))
            except ValueError:
                print("Error: el precio tiene que estar en numeros")
            else:
                return salePrice

    def getKGs(self, name):
        while True:
            print(f"Kgs de {name}:")

            try:
                kgs = int(input(">>"))
            except ValueError:
                print("Los kilogramos deben estar en numeros.")
            else:
                return kgs

    def getOffer(self, name):
        print(f"{name} esta con oferta? S/N")
        offer = input(">>").upper()

        if offer == "S":
            return True
        else:
            return False