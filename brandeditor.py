from general_functions import *


def printFormattedEditorTitle(editingTitle):
    print(f"{editingTitle} o cero(0) para volver al menu de edicion")


class Editor():
    def editorMainMenu(self, brands: dict):
        printTitle("EDITOR DE MARCA\n")

        print("Ingresar una marca para editar (o ingresar 0 para volver al menu principal)")

        editopt = input(">>").title()
        if editopt != "0" and len(editopt) > 0:
            try:
                brand = brands[editopt]
            except KeyError:
                print(f'Error: no existe la marca "{brand}"')
                pausa()
            else:
                self.brandEditorMenu(brand)

    def brandEditorMenu(self, brand: object):
        while True:
            # printTitle("EDITOR DE MARCA\n")
            print(f"Que queres editarle a {brand.name}?\n\t1)Precio de venta\n\t2)Precio de costo\n\t3)kgs")

            editopt = int(input(">>"))
            print()
            if editopt == 1:
                printFormattedEditorTitle("Ingresa el nuevo precio de venta")

                newSalePrice = self.getNewSalePrice()
                confirm_opt = confirmOption()
                if confirmed(confirm_opt):
                    brand.salePrice = newSalePrice
                else:
                    continue
            elif editopt == 2:
                printFormattedEditorTitle("Ingresa el nuevo precio de costo")

                newCostPrice = self.getNewCostPrice()
                confirm_opt = confirmOption()

                if confirmed(confirm_opt):
                    brand.salePrice = newCostPrice
                else:
                    continue
            elif editopt == 3:
                print("Ingresa el nuevo peso en kgs")
                newKgs = self.getNewKgs()

                if newKgs == 0:
                    break
                confirm_opt = confirmOption()
                if confirmed(confirm_opt):
                    brand.kg = newKgs
                else:
                    continue
            else:
                break

    def getNewSalePrice(self):
        while True:
            try:
                newPrice = int(input(">>"))
            except TypeError:
                print("Error: el nuevo precio de venta tiene que estar en numeros")
            else:
                return newPrice

    def getNewCostPrice(self):
        while True:
            try:
                newPrice = int(input(">>"))
            except TypeError:
                print("Error: el nuevo precio de costo tiene que estar en numeros")
            else:
                return newPrice

    def getNewKgs(self) -> int:
        try:
            new_kgs = int(input(">>"))
        except TypeError:
            print("Error: los kgs tienen que estar en numeros")
        else:
            return new_kgs