a,b = input().split()
l1,h1 = input().split()
l2,h2 = input().split()
a = int(a)
b = int(b)
l1 = int(l1)
h1 = int(h1)
l2 = int(l2)
h2 = int(h2)
if (l1+l2<=a and (h1<=b and h2<=b)):
    print ("S")
elif (h1+l2<=a  and l1<=b and h2<=b):
    print ("S")
elif (l1+h2<=a and h1<=b and l2<=b):
    print ("S")
elif (h1+h2<=a and l1<=b and l2<=b):
    print("S")
elif (l1+l2<=b and (h1<=a and h2<=a)):
    print ("S")
elif (h1+l2<=b  and l1<=a and h2<=a):
    print ("S")
elif (l1+h2<=b and h1<=a and l2<=a):
    print ("S")
elif (h1+h2<=b and l1<=a and l2<=a):
    print ("S")
else:
    print ("N")