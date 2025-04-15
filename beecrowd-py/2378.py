a,b = input().split()
a = int(a)
b = int(b)
capacidade = 0 
f = 0 
for i in range (1,a+1):
    c,d = input().split()
    c = int (c)
    d = int (d)
    f = f + (d - c)
    if (f>b):
        capacidade = 1
if (capacidade==1):
    print ("S")
else:
    print("N")