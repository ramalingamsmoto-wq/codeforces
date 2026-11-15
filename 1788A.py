

def process(n,a):
    pre=[1]*n
    suf=[1]*n
    
    pre[0]=a[0]
    for i in range(1,n,1):
        pre[i]=pre[i-1]*a[i]
    
    suf[n-1]=a[n-1]  
    for i in range(n-2,-1,-1):
        suf[i]=suf[i+1]*a[i]
    
    #print(f" pre {pre}")
    #print(f"suf {suf}")
    idx=-1
    for i in range(0,n-1,1):
        if pre[i]==suf[i+1]:
            idx=i+1
            break    
    return idx
    
    
res=[]
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    tans=process(n,a)
    res.append(tans)
for e in res:
    print(e)    
    