dias = int (input())
anos = dias / 365
anos = int (anos)
meses = (dias - 365 * anos) / 30
meses = int (meses)
restante = dias - (365 * anos) - (30*meses) 
diames = restante
print ("%d ano(s)"% anos)
print ("%d mes(es)"% meses)
print ("%d dia(s)"% diames)
