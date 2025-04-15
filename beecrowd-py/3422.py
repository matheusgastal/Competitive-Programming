n = input()
n = int(n)

for _ in range(0, n):
    n = input().split()
    n[0] = int(n[0])
    tempo = n[0]

    if n[1] == "1T":
        if n[0] <= 45: 
            print(n[0])
        if n[0] > 45:
            k = tempo - 45
            print("45+{}".format (k))
    
    if n[1] == "2T":
        if n[0] <= 45:
            print(45+tempo)
        if n[0] > 45:
            k = tempo - 45
            print("90+{}".format (k))