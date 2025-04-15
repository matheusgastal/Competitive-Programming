v = input().split()
v2 = input().split()
nao = 1
for i in range (0,len(v)):
     (v[i]) = int (v[i])
     (v2[i]) = int (v2[i])
     if (v[i] == v2[i]):
         nao = 0
if (nao==1):
    print ("Y")
else:
    print ("N")