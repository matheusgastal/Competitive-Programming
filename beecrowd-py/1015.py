a,b = input().split()
c,d = input().split()

a = float (a)
b = float (b)
c = float (c)
d = float (d)
distancia = ((c-a)**2 + (d-b)**2)**0.5
print ("%.4f" % distancia)