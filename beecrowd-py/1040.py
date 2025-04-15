a,b,c,d = input().split()
a = float (a)
b = float (b)
c = float (c)
d = float (d)
media = (a*2 + b*3 + c*4 + d) / 10 
print ("Media: %.1f" % media)
if (media>7):
    print ("Aluno aprovado.")
elif (media<5.0):
    print ("Aluno reprovado.")
if(5<=media<=6.9):
    print ("Aluno em exame.")
    e = float (input())
    mf = (e + media) / 2
    print ("Nota do exame: %.1f" % e)
    if (mf<5):
        print("Aluno reprovado.")
        print ("Media final: %.1f" % mf )
    else:
        print ("Aluno aprovado.")
        print ("Media final: %.1f" % mf )