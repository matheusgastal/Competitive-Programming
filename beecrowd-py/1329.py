joao = 0
maria = 0 
while (True):
    a = int (input())
    if (a==0):
        break
    joao = 0
    maria = 0
    vA = input().split()
    for i in range (0,a):
        vA[i] = int (vA[i])
        if (vA[i]) == 0:
            maria += 1  
        else:
            joao += 1
    print ("Mary won %d times and John won %d times" % (maria,joao))