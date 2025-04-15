n = input()
n = int(n)
if n<= 10:
    print("7")
elif 11<=n<=30:
    valor_pago = 7 + ((n-10)*1)
    print(valor_pago)
elif 31<=n<=100:
    valor_pago = 7 + 20 + ((n-30)*2)
    print(valor_pago)
else:
    valor_pago = 7 + 20 + 140 + ((n-100)*5)
    print(valor_pago)