a = int (input())
for i in range (1,a+1):
    b = int (input())
    c,d,e,f = input().split()
    c = int (c)
    d = int (d)
    e = int (e)
    f = int (f)
    g = int (input())
    if (b!= c and d and e and f and g) and (c!= d and e and f and g) and (d!= e and f and g) and (e != f and g) and (f!=g):
        if(b<7 and c<7 and d<7 and e<7 and f<7 and g<7):
            if (b+g==7 and c+e==7 and f+d==7):
                print ("SIM")
            else:
                print ("NAO")
        else:
            print ("NAO")
    else:
        print ("NAO")