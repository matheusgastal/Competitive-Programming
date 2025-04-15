def euclides (a,b):
    while b!= 0:
        a,b = b, a%b 
    return a 
while True:
    try:
        m = int(input())
        a1,a2,a3 = map (int,input().split())
        
        mdc0 = euclides(a1,a2)
        mmc0 = a1*a2 // mdc0
        mdc1 = euclides(mmc0,a3)
        ano = mmc0 * a3 // mdc1
        
        print (ano-m)
    except EOFError:
        break
        