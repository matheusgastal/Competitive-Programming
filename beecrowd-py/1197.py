while True:
    try:
        a,b = input().split()
        a = int (a)
        b = int (b)
        print ((a*2) *b)
    
    except EOFError:
        break