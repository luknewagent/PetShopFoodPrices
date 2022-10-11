from general_functions import *

brands = {}


def showBrands(brands):
    printTitle("VISUALIZADOR DE MARCAS")

    for brand in brands.values():
        print(brand)
    input()


def showBrandsPrice(brand):
    printTitle("PRECIOS DE MARCA")
    print(f"Nombre: {brand.name}, Precio por kg: {brand.get_KG_price('salePrice')}")