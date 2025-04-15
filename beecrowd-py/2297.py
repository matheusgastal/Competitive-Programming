c = 0
d = 0 
for n in range (1,1000):   
    j = int(input())
    c = 0  
    d = 0 
    if (j==0):
        break
    for i in range (1,j+1):
        a,b = input().split()
        a = int(a)
        b = int (b)
        if (a>b):
            c = c + (a-b)
        if (b>a):
            d = d + (b-a)
    print ("Teste %d" % n)
    if (c>d):
        print("Aldo")
    else:
        print ("Beto")
    print ("")