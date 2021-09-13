l=[]

def decBin():
    n=int(input("Ingrese el numero binario a transformar\n"))
    print('El numero decimal',n,end=' ')
    while(n>=1):
        l.append(n%2) #residuo de la division de n en 2
        n=int(n//2)
    s=l[::-1] #se invierte la lista
    print("Corresponde a ",s, "en binario")