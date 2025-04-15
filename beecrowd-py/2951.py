a, b = input().split()
a = int(a)
b = int(b)

dicionario = {}

for _ in range(a):
    a1, b1 = input().split()
    b1 = int(b1)
    dicionario[a1] = b1

x = int(input())

soma = 0
letra = input().split()
for p in range(0, x):
    let = letra[p]
    soma += dicionario[let]
    
    
print(soma)
if soma < b:
    print("My precioooous")
else:
    print("You shall pass!")