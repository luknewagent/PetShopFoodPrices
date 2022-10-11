import json
from general_functions import *
from brands_data import showBrandsPrice


class Scales:
    def __init__(self):
        self.moneySale = 0
        self.moneyPurchase = 0
        self.soldSaleSum = 0
        self.soldPurchaseSum = 0
        self.totalEarned =  0

        try:
            self.loadEarned()
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def calculateMenu(self, brands):
        printTitle("CALCULADORA CON BALANZA")
        print("Ingresa una marca o cero(0) para volver al menu de edicion")

        brand_to_calculate = self.getBrandToCalculate(brands)
        if brand_to_calculate != "0" and brand_to_calculate != "" and brand_to_calculate is not None:
            showBrandsPrice(brand_to_calculate)
            print()
            self.calculateSoldGrams(brand_to_calculate, brands)
            self.sumMoney()
            self.saveEarned()

    def calculateSoldGrams(self, brand, brands: dict):
            print(f"GRAMOS A CALCULAR\n")
            while True:
                try:
                    grams_sold = int(input(">>"))
                except ValueError:
                    print("Error: los gramos tienen que estar en numeros")
                else:
                    self.moneySale = brand.get_ANYKG_price(grams_sold, "salePrice")
                    self.moneyPurchase = brand.get_ANYKG_price(grams_sold, "purchasePrice")
                    print(f"Dinero de venta: ${self.moneySale}")
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

    def sumMoney(self):
        self.soldPurchaseSum += self.moneyPurchase
        self.soldSaleSum += self.moneySale
        self.totalEarned = self.soldSaleSum - self.soldPurchaseSum

    def showEarned(self):
        print(f"lo ganado hasta ahora es: ${self.totalEarned}")

    def saveEarned(self):
        moneyEarned = {
            "Money Sale": self.moneySale,
            "Money Purchase": self.moneyPurchase,
            "Sold Sale Sum": self.soldSaleSum,
            "Sold Purchase Sum": self.soldPurchaseSum,
            "Total Earned": self.totalEarned
            }

        with open(f'scalesData/money_earned.json', 'w') as f:
            json.dump(moneyEarned, f, indent=4)

    def loadEarned(self):
        with open(f"scalesData/money_earned.json", "r") as x:
            earnedData = json.load(x)
            self.moneySale = earnedData["Money Sale"]
            self.moneyPurchase = earnedData["Money Purchase"]
            self.soldSaleSum = earnedData["Sold Sale Sum"]
            self.soldPurchaseSum = earnedData["Sold Purchase Sum"]
            self.totalEarned = earnedData["Total Earned"]