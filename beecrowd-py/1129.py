vB = ["A","B","C","D","E"]
erro1 = 0
erro2 = 0 
v = 0 
while (True):
    soma = 0 
    a = int (input())
    if (a==0):
        break
    for i in range (1,a+1):
        erro1 = 0 
        erro2 = 0 
        vA = input().split()
        for n in range (0, len(vA)):
            vA[n] = int (vA[n])
            v = vA[n]
            if(v<=127):
                erro1 +=1
            if (v>127):
                erro2 +=1
            if (v<=127 and erro1<=1 and erro2<=5):
                soma = (vB[n]) 
        if (erro1<=1 and erro2<5):
            print (soma)
        else:
            print ("*")
        