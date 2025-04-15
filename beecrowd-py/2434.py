a,b = input().split()
a = int (a)
b = int(b)
d = b
for i in range (1,a+1):
    c = int (input())
    b = b + c 
    if (b<d):
       d = b 
print (d)