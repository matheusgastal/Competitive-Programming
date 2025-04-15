l = input()
f = input().split()
palavras = 0 
tamanho = len(f)
v = []
for i in range (0,len(f)):
    v = f[i]
    for z in range (0,len(v)):
        if v[z] == l:
            palavras += 1 
            break
resultado = (palavras  * 100) / tamanho
resultado = float(resultado)
print("%.1f" % resultado)