a = int (input())
for i in range (1,a+1):
    a,b,c,d,e,f = input().split()
    a = int (a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int (e)
    f = int(f)
    g = ((a*d + c*f + e*b) + (-(a*f + e*d + c*b)))
    g = g/2
    g = float (g)
    if (g<0):
        g = g * -1
    print ("%.3f" % g)