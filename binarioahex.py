from os import system
import numpy as np

def binHex():
    v = 0
    i = 0
    n=int(input("Ingrese el numero binario a transformar\n"))
    print('El numero binario',n,end=' ')
    while(n>=1):
        d=n%10 #residuo de la division de n en 10
        n=int(n//10) 
        v=v+d*pow(2,i)
        i=i+1
    print("es ",v, "en numero")

    #def deciHex():
    resultado = ""
    # n=int(input("Ingrese el número binario\n"))

    while(  n>0):
        acum = 0
        cont = 0

        while(cont<4):
            aux = n%10

            if(aux == 1):
                if(cont==0):
                    acum = acum + 1

                elif(cont==1):
                    acum = acum + 2

                elif(cont==2):
                    acum = acum + 4

                elif(cont==3):
                    acum = acum + 8

            n = n/10
            cont = cont + 1

        if(acum<=9):
            resultado= str(acum) + resultado
        elif(acum>9):
            if(acum==10):
                resultado="A"+resultado
            elif(acum==11):
                resultado="B"+resultado
            elif(acum==12):
                resultado="C"+resultado
            elif(acum==13):
                resultado="D"+resultado
            elif(acum==14):
                resultado="E"+resultado
            elif(acum==15):
                resultado="F"+resultado

    resultado = "0x" + resultado
    a = hex(v)
    print("Resultado en hexadecimal es: ", a)
                





# while True:
#     residuo = numero%16
#     resultado = int(numero//16)
#     digitoex.append(residuo)
#     numero = resultado
#     i = i + 1
#     if(resultado < 15):
#         break
# j=i
# digitoex.append(residuo)
# print("El valor del resultado ahora es: ",resultado)
# print("El valor en hexanumero es: ")
# while(j==i):
#     if(digitoex[j]==10):
#         print("A",end=' ')
#     elif(digitoex[j] == 11):
#         print("B",end=' ')
#     elif(digitoex[j] == 12):
#         print("C",end=' ')
#     elif(digitoex[j] == 13):
#         print("D",end=' ')
#     elif(digitoex[j] == 14):
#         print("E",end=' ')
#     elif(digitoex[j] == 15):
#         print("F",end=' ')
#     elif(j <= 0):
#         break
#     else:
#         print(str(digitoex[j]),end=' ')

#     j = j - 1


      