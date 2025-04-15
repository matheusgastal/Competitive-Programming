a = int(input())
dic = {}
for i in range (a):
    n,a1,a2,a3 = input().split()
    dic[n] = a1,a2,a3
while True:
    try:
        nm,pres = input().split()
        if nm in dic and pres in dic.get(nm,0):
            print ("Uhul! Seu amigo secreto vai adorar o/")
        else:
            print("Tente Novamente!")
    except EOFError:
        break