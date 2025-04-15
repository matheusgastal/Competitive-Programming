a = int(input())
b = 1
while (a>=b):
    n = int (input())
    l = a - 1
    while (l<a):
        if (n > 0 and n%2 == 0):
            print ("EVEN POSITIVE")
        elif (n<0 and n%2 == 0):
            print ("EVEN NEGATIVE")
        elif (n>0 and n%2 != 0):
            print ("ODD POSITIVE")
        elif (n<0 and n%2 != 0):
            print ("ODD NEGATIVE")
        else:
            print ("NULL")
        l = l+1
        b = b+1
        