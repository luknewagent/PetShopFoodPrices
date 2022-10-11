import json

class CashRegister:
    def __init__(self):
        self.moneySale = 0
        self.moneyCost = 0
        self.soldSaleSum = 0
        self.soldCostSum = 0
        self.totalEarned =  0

        try:
            self.loadEarned()
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass

    def sumMoney(self):
        self.soldCostSum += self.moneyCost
        self.soldSaleSum += self.moneySale
        self.totalEarned = self.soldSaleSum - self.soldCostSum

    def showEarned(self):
        print(f"La ganancia real hasta ahora es: ${self.totalEarned}")

    def saveEarned(self):
        moneyEarned = {
            "Money Sale": self.moneySale,
            "Money Purchase": self.moneyCost,
            "Sold Sale Sum": self.soldSaleSum,
            "Sold Cost Sum": self.soldCostSum,
            "Total Earned": self.totalEarned
            }

        with open(f'scalesData/money_earned.json', 'w') as f:
            json.dump(moneyEarned, f, indent=4)

    def loadEarned(self):
        with open(f"scalesData/money_earned.json", "r") as x:
            earnedData = json.load(x)

            self.moneySale = earnedData["Money Sale"]

            self.moneyPurchase = earnedData["Money Cost"]

            self.soldSaleSum = earnedData["Sold Sale Sum"]

            self.soldCostSum = earnedData["Sold Cost Sum"]

            self.totalEarned = earnedData["Total Earned"]


cashRegister = CashRegister()