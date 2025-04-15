faltaVoltar = [None] * 10001 

while True:
    try:
        n, r = input().split()
        n = int(n)
        r = int(r)
        
        mergulhadores = input().split()
        
        for i in range(1, n+1):
            faltaVoltar[i] = True
        

        for m in mergulhadores:
            faltaVoltar[int(m)] = False
        
       
        todosVoltaram = True
        for i in range(1, n+1):
            if faltaVoltar[i]:
                print("%d " % (i), end='')
                todosVoltaram = False 
                
        if todosVoltaram:
            print("*")
        else:
            print("")
        
    except EOFError:
        break