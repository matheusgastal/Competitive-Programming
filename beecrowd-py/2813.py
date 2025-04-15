a = int(input())
tenhocasa = 0 
tenhotrabalho = 0 
comprartrabalho = 0 
comprarcasa = 0 
for i in range (1,a+1):
    c,t = input().split()
    if c == "chuva":
        if tenhocasa > 0:
            tenhocasa -= 1 
            tenhotrabalho += 1 
        else:
            comprarcasa +=1 
            tenhotrabalho +=1
    if t=="chuva":
        if tenhotrabalho > 0:
            tenhotrabalho -= 1  
            tenhocasa += 1 
        else:
            comprartrabalho +=1 
            tenhocasa +=1 

print ("%d %d" % (comprarcasa, comprartrabalho))