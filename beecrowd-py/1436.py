a = int (input())
for i in range (1,a+1):
    v = input().split()
    v[0] = int(v[0])
    posicao = (v[0] / 2) 
    posicao = int(posicao)
    numero = v[posicao + 1]
    numero = int(numero)
    print ("Case %d: %d" % (i, numero))