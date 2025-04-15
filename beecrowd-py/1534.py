while True:
    try:
        n = input()
        n = int(n)

        mat = [[0] * n for _ in range(n)]
        
        a = n - 1
        for i in range(n):
            mat[i][i] = 1
            mat[i][a] = 2
            a -= 1
        
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0:
                    mat[i][j] = 3
        
        for row in mat:
            print(''.join(map(str, row)))
    
    except EOFError:
        break