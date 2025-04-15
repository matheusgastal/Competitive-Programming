n = input()
mat = [None] * 12
for i in range (0,12):
    mat[i] = [None] * 12
for i in range (0,12):
    for j in range (0,12):
        mat[i][j] = float (input())
tam = 30
soma = 0 
for i in range (0,6):
    for j in range (12-i,12):
        soma += mat[i][j]
for i in range (6,12):
    for j in range (1+i,12):
        soma += mat[i][j]
if n == 'S':
    print (soma)
else:
    print(soma/tam)