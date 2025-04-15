h=0 
m=0
while (True):
    try:

       a,b = input().split()
       a = int (a)
       b = int(b)
       h = a/30
       m = b/6
       if (h<10 and m<10):
           print ("0%d:0%d" % (h,m))    
       elif (h<10 and m>=10):
           print ("0%d:%d" % (h,m))
       elif (h>=10 and m<10):
            print ("%d:0%d" % (h,m))
       else:
            print ("%d:%d" % (h,m))
    except EOFError:
        break
        