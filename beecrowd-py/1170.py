a = int (input())
for i in range (1,a+1):
    c = float(input())
    for n in range (1,1000):
        c = c/2
        if (c<=1):
            print ("%d dias" % n)
            break