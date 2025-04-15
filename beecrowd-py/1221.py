n = int (input())
primo = True
for i in range (n):
    a = int (input())
    if (a==1):
        print ("Prime")
    for p in range (2,201):
        primo = True
        if a!=p:   
            if a%p == 0:
                primo = False
                break
    if (primo == True):
        print ("Prime")
    else:
        print ("Not Prime")