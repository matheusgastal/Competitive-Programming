a = int(input())
for _ in range (1,a+1):
    soma = 0 
    b = input().split()
    tam = len(b)
    b[0] = int(b[0])
    desconto = b[0] - 1  
    for i in range (1,tam):
        b[i] = int(b[i])
        soma += b[i]
    resultado = soma - desconto
    print(resultado)