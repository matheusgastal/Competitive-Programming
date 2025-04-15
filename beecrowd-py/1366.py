while (True):
    c = 0 
    soma = 0 
    a = int (input())
    if a == 0:
        break
    for i in range (0,a):
        vA = input().split()
        for n in range (0,len(vA)):
            vA[1] = int (vA[1])
            c = vA[1] / 2
            c = int(c)
            soma += c
    soma = soma / 4
    soma = int(soma)
    print (soma) 