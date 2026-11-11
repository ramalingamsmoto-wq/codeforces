
from bisect import bisect_left, bisect_right

n=int(input())
a=list(map(int,input().strip().split()))
m=int(input())
res=[]
aux=[0]*n
aux[0]=a[0]
for i in range(1,n,1):
    aux[i]=aux[i-1]+a[i]
    
#print(f"aux {aux}")    
q=list(map(int,input().strip().split()))  
    
for i in range(m):
      
    idx=bisect_left(aux,q[i]) 
    idx+=1
    res.append(idx)
    
for e in res:
    print(e)    