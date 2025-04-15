a = int(input())
repetidas = 0 
mat = [None] * 10000
for j in range (0,10000):
    mat[j] = 0
for i in range(a):
    b = int(input())
    mat[b] += 1
for i in range(0,10000):
    mat[i] = int(mat[i])
    if mat[i] > 1:
        repetidas += mat[i] - 1
print(a-repetidas)
print(repetidas)