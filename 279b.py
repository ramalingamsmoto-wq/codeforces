from bisect import bisect_left

n,t=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
aux=[0]*(n+1)
for i in range(n):
    aux[i+1]=aux[i]+a[i]
mx=-1    
l=len(aux)
#print(f"aux {aux}")
for i in range(1,l,1):
    v=aux[i-1]+t
    #print(f" i {i} v {v}")
    idx=bisect_left(aux, v)
    cnt=0
    if idx<l and  aux[idx]!=v:
        idx=idx-1
    if idx >=l:
        idx=idx-1
            
    if idx==i:
        if a[i-1] >= t:
            cnt=1 
        else:
            cnt=0
    else:
        cnt=idx-i+1
   # print(f"i {i} cnt {cnt}")    
    mx=max(mx,cnt) 
     
print(mx)                    