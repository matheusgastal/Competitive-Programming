l,n = input().split()
l = int(l)
n = int(n)
a = [None] * 21
b = [None] * 21
for z in range (0,l):
    a[z],b[z] = input().split()
for _ in range (0,n):
    palavra = input()
    novetor = False
    for i in range(0,l):
        if palavra == a[i]:
            print (b[i])
            novetor = True
            break
    if novetor == False:
        t = len(palavra)
        if t>1 and palavra[t-1] == 'y' and not (palavra[t-2] == 'a' or palavra[t-2] == 'e' or palavra[t-2] == 'i' or palavra[t-2] == 'o' or palavra[t-2] == 'u'):
           print (palavra[0:t-1] + 'ies')
        elif palavra[t-1] == 'o' or palavra[t-1] == 's' or palavra[t-1] == 'x':
            print (palavra + 'es')  
        elif (palavra[t-1] == 'h' and (palavra[t-2] == 's' or palavra[t-2 == 'c'])):
            print (palavra + 'es')
        else:
            print (palavra + 's')
            