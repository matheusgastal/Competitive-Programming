soma = 0 
m = 4 
for n in range (1,100):
    a = int (input())
    soma = 0
    m = 4
    if (a==-1):
        break
    for i in range (0,a):
        j = 2**i 
        soma += j
    soma += 2
    m = soma**2
    print ("Teste %i" % n)
    print (m)
    print ("")