pedrasocupadas = [None] * 10001
a,b = input().split()
pedras = int(a)
sapos = int(b)
for x in range (0,pedras):
    pedrasocupadas [x] = 0
for n in range (1,sapos+1):
   c,d = input().split()
   posicao = int(c)
   pulo = int(d)
   pedrasocupadas[posicao] =  1
   for i in range (0,pedras):
        if (posicao-pulo>=1):
            ocupada = posicao-pulo 
            posicao = ocupada
            pedrasocupadas[ocupada] = 1
   posicao = int (c)
   for l in range(0,pedras):
        if(posicao+pulo <= pedras):
            ocupada = posicao + pulo
            posicao = ocupada
            pedrasocupadas[ocupada] = 1 
            
for z in range (1,pedras+1):
    if pedrasocupadas[z] == 1:
        print("1")
    else:
        print("0")