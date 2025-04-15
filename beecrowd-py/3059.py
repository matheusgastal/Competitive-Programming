a,b,c = input().split()
a = int(a)
minimo = int(b)
maximo = int(c)
d = input().split()
tam = len(d)
valores = 0 
for i in range(0,tam):
    d[i] = int(d[i])
    for z in range(0,tam):
        d[z] = int(d[z])
        soma = d[z] + d[i]
        if soma>= minimo and soma<= maximo and d[i] != d[z]:
            valores+=1
valores = valores/2
valores = int(valores)
print(valores)
