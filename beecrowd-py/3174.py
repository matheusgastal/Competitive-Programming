n = input()
n = int(n)

import math

bonecos = 0
arquitetos = 0
musicos = 0
desenhistas = 0

for _ in range(0, n):
    egh = input().split()
    egh[2] = int(egh[2])

    if egh[1] == "bonecos":
        k = egh[2]
        bonecos += k
    if egh[1] == "arquitetos":
        k = egh[2]
        arquitetos += k
    if egh[1] == "musicos":
        k = egh[2]
        musicos += k
    if egh[1] == "desenhistas":
        k = egh[2]
        desenhistas += k

bo = math.floor(bonecos/8)
ar = math.floor(arquitetos/4)
mu = math.floor(musicos/6)
de = math.floor(desenhistas/12)


soma = bo + ar + mu + de
print(soma)