f = 1
while (f == 1):
    a,b,c,d = input().split()
    a = int (a)
    b = int(b)
    c = int (c)
    d = int (d)
    if (a>0):
        if (a==c and b==d):
            print ("0")
        if ((a-c == b-d or c-a == b-d) and a!=c and b!=d):
            print ("1")
        if (a==c and b!=d):
            print ("1")
        if (a!=c and b==d):
            print ("1")
        if ((a!=c and b!=d) and a-c != b-d and c-a != b-d):
            print ("2")
    else:
         f = 0