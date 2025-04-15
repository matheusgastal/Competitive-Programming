while (True):
    a = int (input())
    if a == 0:
        break
    v = input().split()
    maior = 0
    segmaior = 0 
    posicao = 0
    for i in range (0,a):
        v[i] = int (v[i])
        if v[i] > maior:
            maior = v[i]
    for n in range (0,a):  
         if (v[n] > segmaior) and (v[n] != maior):
            segmaior = v[n]
            posicao = n + 1
    print (posicao)