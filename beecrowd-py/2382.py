a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
diametro = d*2
e = (a*a + c*c)
d1 = e**0.5
f = (d1*d1 + b*b)
d2 = f**0.5
if (diametro >= d2):
    print ("S")
else:
    print ("N")