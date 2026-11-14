
def process(n,k,a,b):
    a.sort()
    b.sort()
    i=0
    j=n-1
    
    while i<n and j>=0:
        if a[i] < b[j] and k>0:
            temp=a[i]
            a[i]=b[j]
            b[j]=temp
            k=k-1
        else:
            break    
            
        i=i+1
        j=j-1    
    mxs=sum(a) 
    return mxs       


t=int(input())
res=[]
for _ in range(t):
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    b=list(map(int,input().strip().split()))
    tans=process(n,k,a,b)
    res.append(tans)
for e in res:
    print(e)    
    