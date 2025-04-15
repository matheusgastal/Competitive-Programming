a,b, = input().split()
a = int (a)
b = int (b)
if (a>b):  
    resto = a % b
    if (resto == 0):
        print ("Sao Multiplos")
    else:
        print ("Nao sao Multiplos")
if (b>a): 
    resto = b % a
    if (resto == 0):
        print ("Sao Multiplos")
    else: 
        print ("Nao sao Multiplos")