n = input()
n = int(n)

for _ in range(n):
    h, d, g = map(int, input().split())
    if 200<=h<=300 and d>=50 and g>= 150:
        print("Sim")
    else:
        print("Nao")