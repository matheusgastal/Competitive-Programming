soma = 0 
a = int (input())
vA = input().split()
for i in range (0,a):
    vA[i] = int (vA[i])
    if vA[i] == 0:
        soma += 1
if (soma > (a/2)):
    print ("Y")
else:
    print ("N")