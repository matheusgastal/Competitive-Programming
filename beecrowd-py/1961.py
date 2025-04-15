salto,b = input().split()
salto = int(salto)
b = int(b)
v = input().split()
perdeu = 0
for i in range (0,len(v)):
    if (i!= b-1):
        v[i] = int (v[i])
        v[i+1] = int (v[i+1])
        if (v[i]) < v[i+1]:
            if v[i] + salto < v[i+1]:
                perdeu = 1 
        if v[i] > v[i+1]:
            if v[i] - salto > v[i+1]:
                perdeu = 1
if (perdeu==1):
    print ("GAME OVER")
else:
    print ("YOU WIN")