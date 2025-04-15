a = input()
b = input()
igual = True
palavramenor = []
palavramaior = []
if len(a) < len(b):
    maior = len(b)
    menor = len(a)
    palavramenor = a
    palavramaior = b
elif len(b) < len(a):
    maior = len(a)
    menor = len(b)
    palavramenor = b
    palavramaior = a
else: 
    menor = len(a)
for i in range (0,menor):
    if a[i] < b[i]:
        print (a)
        print(b)
        igual = False   
        break
    if b[i] < a[i]:
        print(b)
        print(a)
        igual = False    
        break
if igual == True:
    print (palavramenor)
    print(palavramaior)