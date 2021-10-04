import math
def binDecP():
    v = 0
    x = 0
    i = 0
    j = 0
    n=float(input("Ingrese el numero binario a transformar\n"))

    parte_decimal, parte_entera = math.modf(n)
    cuatro_decimales = round(parte_decimal, 6)
    print("Su parte entera es {} y su parte decimal es {}".format(parte_entera, cuatro_decimales))

    if(len(str(cuatro_decimales))==3):
        cuatro_decimales = cuatro_decimales*10 
        
    elif(len(str(cuatro_decimales))==4):
        cuatro_decimales = cuatro_decimales*100 
        
    elif(len(str(cuatro_decimales))==5):
        cuatro_decimales = cuatro_decimales*1000 
        
    elif(len(str(cuatro_decimales))==6):
        cuatro_decimales = cuatro_decimales*10000

    elif(len(str(cuatro_decimales))==7):
        cuatro_decimales = cuatro_decimales*100000

    elif(len(str(cuatro_decimales))==8):
        cuatro_decimales = cuatro_decimales*1000000
    
    print('El numero binario',n,' es ', end=' ')
    while(n>=1):
        d=n%10 #residuo de la division de n en 10
        n=int(n//10) 
        v=v+d*pow(2,i)
        i=i+1


    while(cuatro_decimales>=1):
        z=cuatro_decimales%10 #residuo de la division de n en 10
        cuatro_decimales=int(cuatro_decimales//10) 
        x=x+z*pow(2,j)
        j=j+1

    print(int(v),".",int(x), "en decimal")