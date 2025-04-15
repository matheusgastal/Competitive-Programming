a = int(input())
v = [None] * 1001
for _ in range(1,a+1):
    palavra = []
    a = input().split()
    v0 = a[0]
    v1 = a[1]
    tv0 = len(v0)
    tv1 = len(v1)
    if tv0>=tv1:
        menor = tv1
        maior = tv0
    elif tv0<tv1:
        menor = tv0
        maior = tv1
    for z in range(0,menor):
        palavra.append (v0[z])
        palavra.append (v1[z])
    if tv0 != tv1:
        for i in range (menor,maior):
            if tv0 > tv1:
                palavra.append(v0[i])
            if tv1 > tv0:
                palavra.append(v1[i])
    palavra = "".join(palavra)
    print (palavra)