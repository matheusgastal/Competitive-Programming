a = int (input())
p = 4
for i in range (1,1000):
    a = a/2
    if (a<2):
        break
    p = p*4
print (p) 