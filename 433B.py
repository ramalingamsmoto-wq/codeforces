


def process(type,l,r):
    if type==1:
        return aux1[r]-aux1[l-1]
    return aux2[r] - aux2[l-1]   

n=int(input())
a=list(map(int,input().strip().split()))
res=[]

aux1=[0]*(n+1)
aux1[1]=a[0]
for i in range(2,n+1,1):
    aux1[i]=aux1[i-1]+a[i-1]
    
a.sort()    
aux2=[0]*(n+1)
aux2[1]=a[0]
for i in range(2,n+1,1):
    aux2[i]=aux2[i-1]+a[i-1]    
    


m=int(input())
for _ in range(m):
    type,l,r=map(int,input().strip().split())
    tans=process(type,l,r)
    res.append(tans)
for e in res:
    print(e)    