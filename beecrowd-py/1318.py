qtbilhete = [None] * 10001 
while True:
    a,b = input().split()
    a = int(a)
    b = int(b)
    
    if a==0 and b==0:
        break
    
    vetor = input().split()
    
    
    for i in range (1,a+1):
        qtbilhete[i] = 0
    
    for p in vetor:
        qtbilhete[int(p)] +=1
    
    falsos = 0 
    for i in range(1,a+1):
        if qtbilhete[i] > 1:
            falsos +=1
    print(falsos)
        