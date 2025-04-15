a = int(input())
for i in range(a):
    s = input()
    b = "" 
    for x in range(len(s)-1,-1,-1):
        if s[x].islower(): 
            b += s[x] 
    print(b)