n,k=map(int,input().strip().split())
a=list(map(int,input().strip().split()))
limit=(2**35)
mn=limit
idx=-1
l=len(a)
aux=[0]*l
aux[0]=a[0]
for i in range(1,l,1):
    aux[i]=aux[i-1]+a[i]
    
#print(f" aux {aux}")    
for i in range(k-1,l,1):
    v1=aux[i]
    #print(f" v1 {v1}")
    if i-k >= 0:
        v1=v1-aux[i-k]
    #print(f" i {i} v1 {v1} ix {i-k}")    
    if v1 < mn:
        mn=v1
        idx=i-k+2    
        
print(idx)        