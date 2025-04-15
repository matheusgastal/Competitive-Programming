n,m,s = input().split()
n = int(n)
m = int(m)
s = int(s)
exercito1=0
exercito2=0
coefangular = m/n 
var1 = coefangular * (-n)
var = var1 + m
for i in range (0,s):
    soldado = input().split()
    soldado[0] = int(soldado[0])
    soldado[1] = int(soldado[1])
    soldado[2] = int(soldado[2])
    padrao = var + coefangular*soldado[0]
    if padrao < soldado[1]:
        exercito1 += soldado[2]
    else:
        exercito2 += soldado[2]
print("%d %d" % (exercito1, exercito2))