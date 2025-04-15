rafael = 0  
beto = 0
carlos = 0 
a = int (input())
for i in range (1,a+1):
    x,y = input().split()
    x = int(x)
    y = int(y)
    rafael = (((3*x)**2) + y**2)
    beto = ((2*(x**2)) + ((5*y)**2))
    carlos = ((-100 * x) + y**3)
    if (carlos>rafael and carlos>beto):
        print ("Carlos ganhou")
    if (rafael>carlos and rafael>beto):
        print ("Rafael ganhou")
    if(beto>carlos and beto>rafael):
        print ("Beto ganhou")