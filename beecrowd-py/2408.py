a,b,c,= input().split()
a = int(a)
b = int(b)
c = int(c)
if (a<b and a>c or a>b and a<c):
    print ("%d" % a)
elif (b>a and b<c or b<a and b>c):
    print ("%d" % b)
elif (c>a and c<b or c<a and c>b):
    print ("%d" % c)