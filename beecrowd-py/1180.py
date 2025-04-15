menor = 10000
posicao = 0 
a = int(input())
v = input().split()
for i in range (0,a):
    v[i] = int (v[i])
    if v[i] < menor:
        menor = v[i]
        posicao = i 
print("Menor valor: %d" % menor)
print ("Posicao: %d" % posicao)
        