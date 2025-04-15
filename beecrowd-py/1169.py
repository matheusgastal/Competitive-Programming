gramas = 0 
graos = 1
kg = 0
a = int (input())
for i in range (1,a+1):
    c = int(input())
    graos = (2**c) - 1
    gramas = graos / 12
    gramas = int (gramas)
    kg = gramas / 1000
    kg = int (kg)
    print ("%d kg" % kg)