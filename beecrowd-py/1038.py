a,b = input().split()
a = int (a)
b = int (b)
if (a==1):
    a = 4
elif (a==2):
    a = 4.5
elif (a==3):    
    a = 5
elif (a==4): 
    a = 2.0
elif (a==5):
    a = 1.5
print ("Total: R$ %.2f" % (a*b))