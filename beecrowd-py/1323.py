f = True
soma = 0
while (f==True):
    soma = 0
    a = int (input())
    for i in range (1,a+1):
        quadrado = i**2
        soma += quadrado
    if (a==0):
        f = False    
        break
    print (soma)