a,b = input().split()
a = int(a)
b = int(b)
marcouEmTodas = 0
jogadores = 0
mat = [None] * 101
for i in range (0,a):
        mat = input().split()
        marcouEmTodas = 0 
        for j in range (0,b):
            mat[j] = int(mat[j])
            if mat[j] >= 1:
                marcouEmTodas += 1 
        if marcouEmTodas == b:
            jogadores +=1
print(jogadores)