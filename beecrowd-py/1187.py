c =input()
mat = [None] * 12
for i in range (0,12):
    mat[i] = [None] * 12
for i in range (0,12):
    for j in range (0,12):
        mat[i][j] = float (input())

soma = 0 
qtde = 30
for i in range (0,5):
    for j in range (1+i,11-i):
        soma += mat[i][j]
if c == 'S':
    print("%.1f" % soma)
else:
    print ("%.1f" % (soma/qtde))