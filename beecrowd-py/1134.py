f = True
alcool = 0
gasolina = 0
diesel = 0
while (f == True):
    a = int (input())
    if (a == 1):
        alcool += 1
    if (a == 2):
        gasolina += 1 
    if (a == 3):
        diesel += 1 
    if (a==4):
        f = False
print ("MUITO OBRIGADO")
print ("Alcool: %d" % alcool)
print ("Gasolina: %d" % gasolina)
print ("Diesel: %d"% diesel)