f = False
while (f == False):
    for i in range (1,1000):
        a = int (input())
        n50 = 0
        n10 = 0 
        n5 = 0
        n1 = 0
        dinheiro = a
        if (dinheiro/50>=1):
            n50 = dinheiro/50
            n50 = int (n50)
            dinheiro = dinheiro - 50*n50
            
        if (dinheiro/10>=1):
            n10 = dinheiro / 10
            n10 = int (n10)
            dinheiro = dinheiro - 10*n10
            
        if (dinheiro/5>=1):
            n5 = dinheiro / 5
            n5 = int (n5)
            dinheiro = dinheiro - 5 * n5
           
        if (dinheiro>=1):
            n1 = dinheiro 
            n1 = int (n1)
        if (a==0):
            f = True
            break
        print ("Teste %d" % i)
        print ("%d %d %d %d" % (n50,n10,n5,n1))
        print ("")