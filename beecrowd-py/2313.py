a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a+b>c and a+c>b and c+b>a):
    if (a==b==c):
        print ("Valido-Equilatero")
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
            print ("Retangulo: S")
        else:
            print("Retangulo: N")
    if (a==b and a!=c or a==c and a!=b or b==c and b!=a):
        print ("Valido-Isoceles")
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
            print ("Retangulo: S")
        else:
            print("Retangulo: N")
    if (a!=b and a!=c and b!=c):
        print ("Valido-Escaleno")
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
            print ("Retangulo: S")
        else:
            print("Retangulo: N")
else:
    print("Invalido")