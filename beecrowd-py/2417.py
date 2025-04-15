a,b,c,d,e,f= input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
#a = vitoriaa b=empatea c=saldoa  d=vitoriab e=empateb f=saldob
if ((a*3)+b > (d*3)+e):
    print ("C")
if ((3*d)+e > (a*3)+b):
    print ("F")
if ((3*d)+e == (3*a)+b):
    if(c>f):
        print("C")
    elif (f>c):
        print("F")
    else:
        print ("=")
        