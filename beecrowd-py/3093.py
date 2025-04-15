a = int(input())
for _ in range (1,a+1):
    q = 0 
    j = 0
    k = 0
    a1 = 0
    a = input()
    for i in range (0,len(a)):
        if a[i] == "Q":
            q = 1 
        if a[i] == 'J':
            j = 1  
        if a[i] == 'K':
            k = 1 
        if a[i] == 'A':
            a1 = 1 
    if q==1 and j==1 and k==1 and a1 ==1:
        print("Aaah muleke")
    else:
        print("Ooo raca viu")