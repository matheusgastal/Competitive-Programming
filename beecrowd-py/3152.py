def calcular_area(vertices):
    n = len(vertices)
    areatotal = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        areatotal += (x1 * y2 - x2 * y1)

    return abs(areatotal) / 2

verticesA = []
verticesB = []

for _ in range(4):
    x, y = map(int, input().split())
    verticesA.append((x, y))
for _ in range(4):
    x, y = map(int, input().split())
    verticesB.append((x, y))

area1 = calcular_area(verticesA)
area2 = calcular_area(verticesB)


if area2 > area1:
    print("terreno B")
else:
    print("terreno A")