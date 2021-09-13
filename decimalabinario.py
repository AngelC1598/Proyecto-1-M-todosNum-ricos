v = 0
i = 0

n=int(input("Ingrese el numero binario a transformar\n"))
print('El numero binario',n,end=' ')
while(n>=1):
    d=n%10
    n=int(n//10)
    v=v+d*pow(2,i)
    i=i+1
print(v, "en decimal")