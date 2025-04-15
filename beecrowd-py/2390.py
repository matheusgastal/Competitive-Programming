a = int (input())
inicio = 0 
soma = 0
for i in range (1,a+1):
    b = int (input())
    if (i==1):
        inicio = b
        c = inicio
        if (inicio>0):
            soma = soma + inicio 
    if (i!=1 and b-c>10):
        soma = soma + (b - c) - 10
        c = b
    else:
        c=b
res = b - soma + 10
print (res)