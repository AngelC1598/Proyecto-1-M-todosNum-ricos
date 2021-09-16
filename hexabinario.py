def obtenerDigito(digit):
    digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for x in range(len(digits)):
        if digit == digits[x]:
            return x
def hexaDec():
    hexNum = str(input("Ingrese el valor en hexadecimal\n"))
    decNum = 0
    power = 0
    for digit in range(len(hexNum),0,-1):
        decNum = decNum + 16 ** power * obtenerDigito(hexNum[digit-1])
        power = power + 1
    print("El valor en decimal es: ",str(decNum))
    decBin(decNum)

def decBin(n):
    l=[]
    while(n>=1):
        l.append(n%2) #residuo de la division de n en 2
        n=int(n//2)
    s=l[::-1] #se invierte la lista
    print("Corresponde a ",s, "en binario")