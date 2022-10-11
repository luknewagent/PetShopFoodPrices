import json
from general_functions import *
from brands_data import showBrandsPrice
from cash_register import cashRegister


class Scales:
    def calculateMenu(self, brands):
        printTitle("CALCULADORA CON BALANZA")
        print("Ingresa una marca o cero(0) para volver al menu de edicion")

        brand_to_calculate = self.getBrandToCalculate(brands)
        if brand_to_calculate != "0" and brand_to_calculate != "" and brand_to_calculate is not None:
            showBrandsPrice(brand_to_calculate)
            print()
            self.calculateSoldGrams(brand_to_calculate, brands)
            cashRegister.sumMoney()
            cashRegister.saveEarned()

    def calculateSoldGrams(self, brand, brands: dict):
            print(f"GRAMOS A CALCULAR\n")
            while True:
                try:
                    grams_sold = int(input(">>"))
                except ValueError:
                    print("Error: los gramos tienen que estar en numeros")
                else:
                    cashRegister.moneySale = brand.get_ANYKG_price(grams_sold, "salePrice")
                    cashRegister.moneyCost = brand.get_ANYKG_price(grams_sold, "costPrice")
                    print(f"Dinero de venta: ${cashRegister.moneySale}")
                    pausa()
                    break

    def getBrandToCalculate(self, brands):
        brand = input(">>").title()
        try:
            brand = brands[brand]
        except KeyError:
            print()
            print("Error: esa marca no existe.")
            pausa()
        else:
            return brand
