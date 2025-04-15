n = input()
n = int(n)
multiplicacao = n*n 
 
if multiplicacao%2 == 0:
    metade = multiplicacao/2
    metade = int(metade)
    print("{} casas brancas e {} casas pretas". format (metade, metade))
else:
    metade = multiplicacao/2
    metade = round(metade)
    metade1 = metade + 1 
    metade = int(metade)
    metade1 = int(metade1)
    print("{} casas brancas e {} casas pretas". format (metade1, metade))