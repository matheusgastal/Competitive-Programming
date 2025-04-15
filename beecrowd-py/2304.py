a,b = input().split()
a = int(a)
b = int(b)
d = a
e = a 
f = a 
for i in range (0,b):
    v = input().split()
    if v[0] == 'C':
        v[2] = int (v[2])
        if v[1] == 'D':
            d-=v[2]
        elif v[1] == 'E':
            e-=v[2]    
        else:
          f-=v[2]  
    if v[0] == 'V':
        v[2] = int (v[2])
        if v[1] == 'D':
            d+=v[2]
        elif v[1] == 'E':
            e+=v[2]    
        else:
            f+=v[2] 
    if v[0] == 'A':
        if v[1] == 'D':
            v[3] = int(v[3])
            if v[2] == 'E':
                d+=v[3]
                e-=v[3]
            if v[2] == 'F':
                d+=v[3]
                f-=v[3]
        if v[1] == 'E':
            v[3] = int(v[3])
            if v[2] == 'D':
                e+=v[3]
                d-=v[3]
            if v[2] == 'F':
                e+=v[3]
                f-=v[3]
        if v[1] == 'F':
            v[3] = int(v[3])
            if v[2] == 'D':
                f+=v[3]
                d-=v[3]
            if v[2] == 'E':
                f+=v[3]
                e-=v[3]
print("%d %d %d" % (d,e,f))
            
            