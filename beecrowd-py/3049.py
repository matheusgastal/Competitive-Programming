b = int (input())
t = int (input())
felix = (b+t) *35
marzia = ((160-b) + (160-t)) * 35
if (felix>marzia):
    print ("1")
elif felix < marzia:
    print ("2")
else:
    print ("0")