from os import system
from decimalabinario import decBin
from binarioadecimal import binDec
from binarioahex import binHex
from hexabinario import hexaDec
from decimalabinconpunto import decBinP
from binarioadeciconpunto import binDecP



print("Bienvenido a la calculadora binaria")
input()

menu = 0
while menu != 6:
    print("----------------Calculadora de Matrices----------------")
    print("\nSeleccione la opcion a realizar\n")
    print("1. Decimal a Binario\n","2. Binario a Decimal\n", "3. Binario a Hexadecimal\n", "4. Hexadecimal a Binario\n","5. Decimal a binario con punto flotante\n" ,"6. Binario a decimal con punto flotante\n","7. Salir\n")
    menu = int(input("Ingresa una opcion: "))
    input()

    if menu == 1:
        decBin()
        input()
        system("cls")
    elif menu == 2:
        binDec()
        input()
        system("cls")
    elif menu == 3:
        binHex()
        input()
        system("cls")
    elif menu == 4:
        hexaDec()
        input()
        system("cls")
    elif menu == 5:
        decBinP()
        input()
        system("cls")
    elif menu == 6:
        binDecP()
        input()
        system("cls")    
    elif menu == 7:
        print("Usted está saliendo del programa...")
        input()
        system("cls")
        break
    else:
        print("La opcion seleccionada no es válida...")
        input()
        system("cls")