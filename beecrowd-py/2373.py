copos = 0 
a = int (input())
for i in range (1,a+1):
    b,c = input().split()
    b = int (b)
    c = int (c)
    if (b>c):
        copos = copos + c
print (copos)