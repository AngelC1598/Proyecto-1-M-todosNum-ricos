import math

def decBinP():
    l=[]
    n=float(input("Ingrese el numero decimal a transformar\n"))
    print('El numero decimal es',n,end=' ')
    parte_decimal, parte_entera = math.modf(n)
    cuatro_decimales = round(parte_decimal, 4)
    print("Su parte entera es {} y su parte decimal es {}".format(parte_entera, cuatro_decimales))

    if(len(str(cuatro_decimales))==3):
            cuatro_decimales = cuatro_decimales*10 
            
    elif(len(str(cuatro_decimales))==4):
            cuatro_decimales = cuatro_decimales*100 
            
    elif(len(str(cuatro_decimales))==5):
            cuatro_decimales = cuatro_decimales*1000 
            
    elif(len(str(cuatro_decimales))==6):
            cuatro_decimales = cuatro_decimales*10000

    cuatro_decimales = round(cuatro_decimales)

    parte_entera = round(parte_entera)
    while(parte_entera>=1):
        l.append(parte_entera%2) #residuo de la division de n en 2
        parte_entera=int(parte_entera//2)
    s=l[::-1] #se invierte la lista
    print("Corresponde a ",s,".",end=" ")

    l=[]
    if(cuatro_decimales > 0):
        while(cuatro_decimales>=1):
            l.append(cuatro_decimales%2) #residuo de la division de n en 2
            cuatro_decimales=int(cuatro_decimales//2)
        x=l[::-1] #se invierte la lista
        print(x,"en binario")
