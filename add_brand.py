from general_functions import *
from brand import Brand
from new_brand_data_getter import *
from general_functions import confirmOption


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

    purchasePrice = getCostPrice(name)
    salePrice = getSalePrice(name)
    kgs = getKGs(name)
    offer = getOffer(name)

    new_brand = Brand(name, purchasePrice, salePrice, kgs, offer)
    brands[name] = new_brand