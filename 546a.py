k,n,w=map(int,input().strip().split())
aux=[0]*(w+1)

aux[1]=k
for i in range(2,w+1,1):
    v=i*k
    aux[i]=aux[i-1]+v
d=aux[w] - n

if d <=0 :
    
    print(0)
else:
    print(d)    
    
    