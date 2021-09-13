from os import system

print("Bienvenido a la calculadora binaria")
input()

menu = 0
while menu != 6:
    print("----------------Calculadora de Matrices----------------")
    print("\nSeleccione la opcion a realizar\n")
    print("1. Decimal a Binario\n","2. Binario a Decimal\n", "3. Binario a Hexadecimal\n", "4. Hexadecimal a Binario\n", "5. Salir\n")
    menu = int(input("Ingresa una opcion: "))
    input()

    if menu == 1:
        input()
        system("cls")
    elif menu == 2:
        input()
        system("cls")
    elif menu == 3:
        input()
        system("cls")
    elif menu == 4:
        input()
        system("cls")    
    elif menu == 5:
        print("Usted está saliendo del programa...")
        input()
        system("cls")
        break
    else:
        print("La opcion seleccionada no es válida...")
        input()
        system("cls")