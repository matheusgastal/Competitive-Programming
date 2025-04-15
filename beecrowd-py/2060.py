a = int (input())
b = input().split()
m2 = 0
m3 = 0
m4 = 0
m5 = 0
for i in range (0,len(b)):
    b[i] = int(b[i])
    if b[i] % 2 == 0:
        m2 += 1
    if b[i] % 3 == 0:
        m3 += 1
    if b[i] % 4 == 0:
        m4 += 1
    if b[i] % 5 == 0:
        m5 += 1
print ("%d Multiplo(s) de 2" % m2)
print ("%d Multiplo(s) de 3" % m3)
print ("%d Multiplo(s) de 4" % m4)
print ("%d Multiplo(s) de 5" % m5)
    