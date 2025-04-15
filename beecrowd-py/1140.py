v = [None] * 10001
while True:
    a = input().split()
    iguais = True
    if a[0] == '*':
        break
    for z in range (0,len(a)):
        v[z] = a[z]
        f = v[z-1]
        g = v[z]
        if z!= 0:
            if f[0].lower() != g[0].lower():
                iguais = False
    if iguais == True:
        print("Y")
    else:
        print("N")