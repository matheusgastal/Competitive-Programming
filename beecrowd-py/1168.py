a = int(input())
for _ in range(1,a+1):
    leds = 0
    numero = input()
    for i in range(0,len(numero)):
        nmr = int (numero[i])
        if nmr == 1:
            leds += 2
        if nmr == 2 or nmr == 3 or nmr == 5:
            leds += 5
        if nmr == 4:
            leds += 4
        if nmr == 6 or nmr == 9 or nmr == 0:
            leds += 6 
        if nmr == 7:
            leds+= 3
        if nmr == 8:
            leds+=7
    print ("%d leds" % leds)