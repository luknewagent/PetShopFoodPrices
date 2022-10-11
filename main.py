from scales import Scales
from brand_editor import Editor
from brand_adder import BrandAdder
from brands_data import brands
from brands_visualizer import *
from save_load import *
from general_functions import printTitle, pausa
from cash_register import cashRegister

scales = Scales()
editor = Editor()
brandAdder = BrandAdder()

# Load brands data
load_brands(brands)

# Main loop
def main():
    while True:
        save_data(brands)

        printTitle("MENU PRINCIPAL")
        print("1)Agregar marca\n2)Editor de marca\n3)Ver marcas\n4)Balanza\n5)Mostrar informacion\n6)Salir\n")

        user_opt = input(">>")

        if user_opt == "1":
            brandAdder.addBrand(brands)
        elif user_opt == "2":
            editor.editorMainMenu(brands)
        elif user_opt == "3":
            showBrands(brands)
        elif user_opt == "4":
            scales.calculateMenu(brands)
        elif user_opt == "5":
            while True:
                printTitle("VISUALIZADOR DE CAJA")
                print("1)Mostrar ganancia real\n")

                opt = input(">>")

                if opt == "1":
                    cashRegister.showEarned()
                    pausa()
                    break
                else:
                    print("opcion invalida")
        elif user_opt == "6":
            printTitle("Estas saliendo del programa...")
            pausa()
            break
        else:
            printTitle("Oops... algo salio mal!")
            print()
            print("La opcion ingresada no es valida.")
            pausa()


if __name__ == '__main__':
    main()