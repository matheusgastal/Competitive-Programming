a = int (input())
p = 100000
for i in range (1,a+1):
    b,c = input().split()
    b = float (b)
    c = int (c)
    d = (1000/c) * b
    if (d<p):
        p = d 
print ("%.2f" % p)
