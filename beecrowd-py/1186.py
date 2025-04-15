c =input()
mat = [None] * 12
for i in range (0,12):
    mat[i] = [None] * 12
for i in range (0,12):
    for j in range (0,12):
        mat[i][j] = float (input())

soma = 0 
qtde = 66
for i in range (0,12):
    for j in range (12-i,12):
        soma += mat[i][j]
if c == 'S':
    print("%.1f" % soma)
else:
    print ("%.1f" % (soma/qtde))
        