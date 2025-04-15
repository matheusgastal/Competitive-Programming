while True:
    try:
        a,b,c = input().split()
        a = int (a)
        b = int (b)
        c = int(c)
        if (a!=c and c==b):
            print("A")
        if (a==c and b!=a):
            print ("B")
        if (a==b and c!=a):
            print ("C")
        if (a==c==b):
            print ("*")
    except EOFError:
        break