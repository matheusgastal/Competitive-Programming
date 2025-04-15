segundos = int (input())
horas = segundos / 3600
horas = int (horas)
minutos = (segundos - horas * 3600) / 60 
minutos = int (minutos)
sec = segundos - (horas*3600) - (minutos*60)
print (horas,minutos,sec, sep=":") 
