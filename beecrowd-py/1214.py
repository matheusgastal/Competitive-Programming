a = int (input())
for i in range (1,a+1):
    soma = 0 
    media = 0 
    alunos = 0 
    acima = 0
    porc = 0
    v = input().split()
    v[0] = int (v[0])
    alunos = v[0]
    for n in range (1,len(v)):
        v [n] = int (v[n])
        soma+=v[n]
    media = soma / alunos
    for z in range (1,len(v)):
        v [z] = int (v[z])
        if v[z] > media:
            acima += 1
    porc = (acima * 100) / alunos
    print ("%.3f%%" %  porc)
            