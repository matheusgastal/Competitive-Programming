a,b,c,= input().split()
a = int(a)
b = int(b)
c = int(c)
d,e = input().split()
d = int(d)
e = int(e)

if  ((a<=e or a<=d) and ((b<=e and b<=d) or (c<=e and c<=d))):
    print ("S")
elif ((b<=e or b<=d) and ((a<=e and a<=d) or (c<= e and c<=d))):
    print ("S")
elif ((c<=e or c<=d) and ((a<= e and a<=d) or (b<= e and b<=d))):
    print ("S")
else:
    print ("N")
    