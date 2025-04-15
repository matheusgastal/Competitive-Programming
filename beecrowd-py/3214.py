e, f, c = map(int, input().split())
total = 0
soma = e + f

while soma >= c:    
    refrigerantes_comprados = soma // c  
    total += refrigerantes_comprados     
    soma = refrigerantes_comprados + (soma % c) 

print(total)