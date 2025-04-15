a = int(input())
v = []
for n in range(0,a):
    b = int(input())
    v.append (b)
   
for i in range(0,len(v)):  
    soma = 0 
    if i!= 0 and i!= len(v) - 1:
        v[i-1] = int (v[i-1])
        v[i] = int (v[i])
        v[i+1] = int (v[i+1])
        soma = v[i] + v[i-1] + v[i+1]
        print(soma)
    if i == 0 and len(v) != 1:
        v[i] = int (v[i])
        v[i+1] = int (v[i+1])
        soma = v[i] + v[i+1]
        print(soma)
    if i==len(v)-1 and i!=0:
        v[i-1] = int (v[i-1])
        v[i] = int (v[i])
        soma = v[i] + v[i-1]
        print(soma)
    if i==0 and a==1:
        v[i] = int (v[i])
        if v[i] == 1:
            print("1")
        else:
            print("0")