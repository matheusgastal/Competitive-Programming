vc = 0
vb = 0
for n in range (1,1000):
    a = int (input())
    vc = 0 
    vb = 0
    if (a==0):
        break
    print ("Teste %d" % n)
    for i in range (1,a+1):
        b,c = input().split()
        b = int (b)
        c = int (c)
        if (c<b):
            vb = vb + (b - c)
        if (c>b):
            vc = vc + (c - b)
        print (vb-vc)
    print ("")