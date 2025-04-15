while True:
    try:
        soma = 0
        sacos = 0
        litros = 0 
        a,b = input().split()
        a = int(a)
        b = int(b)
        for i in range (0,a):
            c = input().split()
            for j in range (0,b):
                c[j] = int(c[j])
                soma += c[j]
        sacos = soma/60
        sacos = int(sacos)
        litros = soma - (sacos*60)
        litros = int(litros)
        print ("%d saca(s) e %d litro(s)" % (sacos,litros))
    except EOFError:
        break