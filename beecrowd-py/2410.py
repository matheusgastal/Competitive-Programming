a = int(input())
soma = 0 
mat = [None] * 1000001
for i in range (0,1000001):
    mat[i] = 0
for i in range(a):
    b = int(input())
    mat[b] += 1
    if mat[b] == 1:
        soma+=1
print(soma)