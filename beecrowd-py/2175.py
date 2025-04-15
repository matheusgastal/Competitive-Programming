a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if (a<b and a<c):
    print ("Otavio")
elif (b<a and b<c):
    print ("Bruno")
elif (c<a and c<b):
    print ("Ian")
elif ((a==b and a<c) or (a<b and a==c) or (b==c and b<a) or (a==b and a==c)):
    print ("Empate")
